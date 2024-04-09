

from mpi4py import MPI
import random
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
total_number_of_processes = comm.Get_size()
number_of_data_points = 1000000

count_right = 0
for _ in range(number_of_data_points):
    x = random.random()*2 - 1
    y = random.random()*2 - 1

    distance_from_zero = math.sqrt(x**2+y**2)
    if distance_from_zero < 1:
        count_right += 1

points_in_circle_count = comm.gather(count_right,root=0)

if rank == 0:
    total_number_points_in_cicle = sum(points_in_circle_count)
    porition_in_circle = total_number_points_in_cicle/(number_of_data_points * total_number_of_processes)
    total_area_of_square = 2 * 2
    area_of_circle = porition_in_circle *total_area_of_square
    print(f"Circle with radius one has this area: {area_of_circle}")

print(f"Process with rank {rank} ending")
