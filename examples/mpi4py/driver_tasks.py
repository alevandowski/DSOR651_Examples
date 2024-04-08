"""MPI Example using class-based tasks

This Python-script based MPI program demonstrates how classes may be used to
represent tasks and MPI messages. The MPI process with rank 0 creates a task
for every other process and sends a message to each process with this task.
Each task is represented as an instance of a Task class, having an execute
method. The other processes receive the task and execute it.

To run this MPI program, execute:

> mpiexec -n 4 python driver_tasks.py

"""

from mpi4py import MPI
import random


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


class FindLargestNumberInFileTask:

    def __init__(self, file_path):
        self.file_path = file_path
    
    def execute(self):
        max_number = None
        with open(self.file_path) as file:
            for r in file:
                try:
                    n = float(r)
                    if max_number is None or n > max_number:
                        max_number = n
                except:
                    print(f"Skipping line '{r}' in {self.file_path}")
        print(f"The largest number is {self.file_path} is {max_number}")
        return max_number


class FindSmallestNumberInFileTask:

    def __init__(self, file_path):
        self.file_path = file_path

    def execute(self):
        min_number = None
        with open(self.file_path) as file:
            for r in file:
                try:
                    n = float(r)
                    if min_number is None or n < min_number:
                        min_number = n
                except:
                    print(f"Skipping line '{r}' in {self.file_path}")
        print(f"The smallest number is {self.file_path} is {min_number}")
        return min_number


if rank == 0:
    file_paths = [f"data/{i}.txt" for i in range(1,5)]
    task_types = [FindLargestNumberInFileTask, FindSmallestNumberInFileTask]
    for rank_to_send_to in range(1,size):

        cls_task_type = random.choice(task_types)
        file_path = random.choice(file_paths)

        task = cls_task_type(file_path)
        comm.send(task,dest=rank_to_send_to)
else:
    task = comm.recv()
    task.execute()
