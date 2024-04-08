'''
    This scripts demonstrates how to compute the area of circle without knowing PI using monte-carlo simulation.
'''

import multiprocessing as mp
import random
import math
import time

results = mp.Queue()

number_of_data_points = 1000000
processes = 10

def run_simulation(number_of_data_points:int, results:mp.Queue):
    count_right = 0
    for _ in range(number_of_data_points):
        x = random.random()*2 - 1
        y = random.random()*2 - 1

        distance_from_zero = math.sqrt(x**2+y**2)
        if distance_from_zero < 1:
            count_right += 1
    
    results.put(count_right)


if __name__ == "__main__":
    mp.freeze_support()
    pts = []
    for i in range(processes):
        pts.append(mp.Process(target=run_simulation,args=(number_of_data_points,results)))

    start = time.time()
    for pt in pts:
        pt.start()

    for pt in pts:
        pt.join()
    
    duration = time.time() - start
    print(f"Duration {duration}")

    sum_points_in_circle = sum([results.get() for _ in range(processes)])
    area = sum_points_in_circle / (number_of_data_points * processes) *(2*2)
    print(f"Area is {area}")