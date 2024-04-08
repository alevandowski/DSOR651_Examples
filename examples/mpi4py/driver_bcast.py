"""MPI Example broadcast example

This Python-script based MPI program demonstrates how a process can send
a message, represented as a Python object, to many other processes.

This example uses MPI's collective communication methods, bcast.

This example also demonstrates how a barrier can be used to sync the 
execution across many processes.

To run this MPI program, execute:

> mpiexec -n 4 python driver_basic.py

"""
from mpi4py import MPI
import random


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data_to_send = tuple(random.randint(0,10) for _ in range(10))
    print(f"Process with rank {rank} sending the following data: {data_to_send}")
    comm.bcast(obj=data_to_send,root=0)
else:
    data_received = comm.bcast(obj=None,root=0)
    print(f"Process with rank {rank} received the following data: {data_received}")

# Notice the difference when the following line is commented out.
comm.Barrier()

# Barrier allows processes in a communicator to sync to a certain point in 
# code. All processes wait for every other process in a communicator to 
# reach the Barrier before continuing.

print(f"Process {rank} has finished.")
