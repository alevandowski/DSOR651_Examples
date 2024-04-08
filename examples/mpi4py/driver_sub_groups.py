"""MPI Example demonstrating Process subsets

This Python-script based MPI program demonstrates how to create a new
Communicator to support communicate with a subset of processes. The 
processes with an odd number rank form a subset of processes. The 
process with rank 0 within this group broadcasts a random number to 
the other processes within this group.

To run this MPI program, execute:

> mpiexec -n 5 python driver_sub_groups.py

"""

from mpi4py import MPI
import random


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank % 2 == 1:
    odd_group = comm.group.Excl([i for i in range(size) if i % 2 != 1])

    odd_group_comm = comm.Create_group(odd_group)
    # print(odd_group_comm.Get_size())

    odd_group_rank = odd_group_comm.Get_rank()

    if odd_group_rank == 0:
        number_to_send = random.random()
        print(f"Process with rank {rank} broadcasting number {number_to_send}.")
        odd_group_comm.bcast(number_to_send)
    else:
        number_received = odd_group_comm.bcast(None)
        print(f"Process with rank {rank} received the following number {number_received}.")
        
else:
    print(f"Process with rank {rank} doing nothing.")
