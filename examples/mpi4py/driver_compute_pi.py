"""MPI Example spawn dynamic sub-processes

From Stack Overflow:
https://stackoverflow.com/questions/32257375/how-to-run-a-basic-mpi4py-code

This Python-script based MPI program demonstrates how a program can spawn
sub-processes dynamically to compute PI. The sub-processes run the script
specified, "cpi.py".

To run this MPI program, execute:

> mpiexec -np 1 python driver_compute_pi.py

"""

from mpi4py import MPI
import numpy
import sys


comm = MPI.COMM_SELF.Spawn(sys.executable,
                           args=['cpi.py'],
                           maxprocs=5)

N = numpy.array(100, 'i')
comm.Bcast([N, MPI.INT], root=MPI.ROOT)
PI = numpy.array(0.0, 'd')
comm.Reduce(None, [PI, MPI.DOUBLE],
            op=MPI.SUM, root=MPI.ROOT)
print(PI)

comm.Disconnect()
