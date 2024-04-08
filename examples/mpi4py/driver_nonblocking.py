"""MPI Example non-blocking send/receive example

This Python-script based MPI program demonstrates how processes send and receive
in a non-blocking manner.  Non-blocking refers to allowing subseqent code to 
execute while the operation continues on in the background.

To run this MPI program, execute:

> mpiexec -n 2 python driver_nonblocking.py

"""
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = numpy.zeros(1)

if rank == 1:
        randNum = numpy.random.random_sample(1)
        print("Process", rank, "drew the number", randNum[0])
        req = comm.Isend(randNum, dest=0)

        # code can be added here while sending is done in background

        req.Wait()
        
if rank == 0:
        print("Process", rank, "before receiving has the number", randNum[0])
        req = comm.Irecv(randNum, source=1)
        
        # code can be added here while receiving is done in background
        
        req.Wait()
        print("Process", rank, "received the number", randNum[0])