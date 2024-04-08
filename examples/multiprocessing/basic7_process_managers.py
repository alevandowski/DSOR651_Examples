'''
    This scripts demonstrates how to use proxy objects to share data between processes.
'''
import time
import multiprocessing
from multiprocessing.managers import BaseManager

class CustomManager(BaseManager):
    # nothing
    pass

def task_cube(n,shared_list):
    print('Sleeping for 0.5 seconds')
    time.sleep(0.5)
    print('Finished sleeping')
    output = n*n*n
    shared_list.append(output)
 
if __name__ == "__main__": 
    start_time = time.time()
    processes = []
    CustomManager.register('list', list)
    with CustomManager() as manager:
        # create a shared set instance
        shared_list = manager.list()
        # Creates 10 processes then starts them
        for i in range(10):
            p = multiprocessing.Process(target = task_cube,args=(i,shared_list))
            processes.append(p)
        
        # Joins all the processes 
        for p in processes:
            p.start()
        for p in processes:  
            p.join()

        shared_list= shared_list._getvalue()
        
        print(shared_list)
    
    finish_time = time.time()
 
    print(f"Program finished in {finish_time-start_time} seconds")
