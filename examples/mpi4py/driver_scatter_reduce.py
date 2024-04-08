"""MPI Example scatter and reduce-all example

To run this MPI program, execute:

> mpiexec -n 4 python driver_scatter_reduce.py
"""

from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

data = None
if rank == 0:
    data = list(range(size))

data = comm.scatter(data, root=0)

result = comm.allreduce(data * rank, op=MPI.SUM)

for i in range(size):
    if (size - i - 1) == rank:
        print(f"Process with rank {rank} has result {result}.")
    import time
    # assume sleep below ensures print above gets sent to
    # console in proper order
    time.sleep(3)
    comm.barrier()
