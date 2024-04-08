"""MPI Example reduce example

This Python-script based MPI program demonstrates how processes can reduce
values to a single value.

This examples uses MPI's collective-compute communication methods, reduce.

To run this MPI program, execute:

> mpiexec -n 4 python driver_basic_reduce.py

"""
from mpi4py import MPI
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

random_number = random.random()

print(f"Process with rank {rank} generated the following number: {random_number}")

reduced_value_min = comm.reduce(random_number, op=MPI.MIN, root=0)
reduced_value_max = comm.reduce(random_number, op=MPI.MAX, root=0)
reduced_value_sum = comm.reduce(random_number, op=MPI.SUM, root=0)

greater_than_half = random_number > 0.5
reduced_value_or = comm.reduce(greater_than_half, op=MPI.BOR, root=0)
reduced_value_and = comm.reduce(greater_than_half, op=MPI.BAND, root=0)

if rank == 0:
    print(f"The min reduced value is: {reduced_value_min}.")
    print(f"The max reduced value is: {reduced_value_max}.")
    print(f"The sum reduced value is: {reduced_value_sum}.")
    print(f"The or reduced value is: {reduced_value_or}.")
    print(f"The and reduced value is: {reduced_value_and}.")
