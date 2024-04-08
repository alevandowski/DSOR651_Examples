"""MPI Example finding the minimum value from numbers pulled from seperate
files

This Python-script based MPI program demonstrates how a program may sort
numbers pulled from seperate files. The Process with rank 0, the coordinator,
scatters a file path, holding the numbers, to each each other process.  These
processes open their assigned file, sort the numbers as they are read
from the file, and then sends their smallest number back through a reduce
operation message. The MPI implementation processes the reduce operation and
only sends the coordinator the smallest value from all the processes.
The coordinator receives the smallest numbers yet to be processed from the 
other processes and adds the smallest of these numbers to a list. This final
list holds the sorted numbers from all the files.

To run this MPI program, execute:

> mpiexec -n 5 python driver_find_min.py

"""

from mpi4py import MPI
from sort_integers_in_file import sort_integers_in_file


comm = MPI.COMM_WORLD
rank = comm.Get_rank()


def return_sorted_numbers_from_file(file_path):
    sorted_integers = sort_integers_in_file(file_path)
    comm.reduce(sorted_integers[0], op=MPI.MIN, root=0)


if rank == 0:
    # first element to scatter is None so that the rank-zero process can execute second stage sort
    data_files_to_sort = [None, "data/1.txt", "data/2.txt", "data/3.txt", "data/4.txt"]
    print(f"Process with rank {rank} sending the following data: {data_files_to_sort}")
    comm.scatter(sendobj=data_files_to_sort, root=0)

    # an artifically large number is provided to allow this process take part
    # in the reduce operation since it does not open a file itself.
    min_value_in_all_files = comm.reduce(999999999, op=MPI.MIN, root=0)
    print(f"Minimum values from all files: {min_value_in_all_files}")     
else:
    data_file_to_sort = comm.scatter(None, root=0)
    print(f"Process with rank {rank} received the following data file to sort: {data_file_to_sort}")
    return_sorted_numbers_from_file(data_file_to_sort)


print(f"Process {rank} has finished.")
