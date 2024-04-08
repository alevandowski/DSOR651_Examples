"""MPI Example send and receive example (seperate scripts)

This Python-script based MPI program demonstrates how a process can send
a message, represented as a Python object, to another process that runs,
based on code from a different python script.

To run this MPI program, execute:

> mpiexec -n 1 python driver_basic_sep_1.py : -n 3 python driver_basic_sep_2.py

"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = {'a': 7, 'b': 3.14}
comm.send(data, dest=1, tag=11)
print(f"Process with rank {rank} sent the following data: {data}")
