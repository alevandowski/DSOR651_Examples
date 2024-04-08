"""MPI Example sorting numbers pulled from seperate files

This Python-script based MPI program demonstrates how a program may sort
numbers pulled from seperate files. The Process with rank 0, the coordinator,
scatters a file path, holding the numbers, to each each other process.  These
processes open their assigned file, first sort the numbers as they are read
from the file, and then sequentially send the sorted numbers back one-at-time.
The coordinator receives the smallest numbers yet to be processed from the 
other processes and adds the smallest of these numbers to a list. This final
list holds the sorted numbers from all the files.

To run this MPI program, execute:

> mpiexec -n 5 python driver_sort.py

"""

from mpi4py import MPI
from sort_integers_in_file import sort_integers_in_file


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def find_min_with_index(lst):
    min_so_far = lst[0]
    min_index = 0
    
    for i, v in enumerate(lst):
        if v[1] < min_so_far[1]:
            min_index = i
            min_so_far = v
    
    return (min_index, min_so_far)


def perform_second_stage_sort():
    completion_count = 0
    values = []
    final_sort = []

    for from_rank in range(1,5):
        v = comm.recv(source=from_rank)
        # This line tracks the rank of the process to support pulling the next
        # number from this process after this value has been added to the final
        # list.
        values.append((from_rank, v))

    while True:
        min_index, value_tuple = find_min_with_index(values)
        del values[min_index]
        min_value = value_tuple[1]
        from_rank = value_tuple[0]

        final_sort.append(min_value)

        # Pull the next smallest value from this source
        v = comm.recv(source=from_rank)
        if v is None:  # no more numbers from this file
            completion_count = completion_count + 1
        else:
            values.append((from_rank, v))
    
        if completion_count == 4:
            break
    
    print(final_sort)
    

def return_sorted_numbers_from_file(file_path):

    sorted_integers = sort_integers_in_file(file_path)

    for integer in sorted_integers:
        comm.send(integer,dest=0)

    # None is sent to the coordinator to indicate no more numbers to sort
    comm.send(None, dest=0)


if rank == 0:
    # first element to scatter is None so that the rank-zero process can execute second stage sort
    data_files_to_sort = [None, "data/1.txt", "data/2.txt", "data/3.txt", "data/4.txt"]
    print(f"Process with rank {rank} sending the following data: {data_files_to_sort}")
    comm.scatter(sendobj=data_files_to_sort, root=0)

    perform_second_stage_sort()    
        
else:
    data_file_to_sort = comm.scatter(None, root=0)

    print(f"Process with rank {rank} received the following data file to sort: {data_file_to_sort}")

    return_sorted_numbers_from_file(data_file_to_sort)


print(f"Process {rank} has finished.")
