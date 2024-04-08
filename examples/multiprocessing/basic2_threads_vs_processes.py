'''
This scripts demonstrates how threads and processes are started in a similar manner.
Note that Python threads run concurrently and not in parallel.
Notice that when child processes are created the console outputs gets mixed up sometimes.
This may not occur with threads unless the Python implementation forces preemption. 
Also, Python threads may not pause to let another sibling thread execute unless a 
instruction executed in the active thread tells it to pause, such as time.sleep().
'''
import multiprocessing as mp
import threading
import time
import os

use_threads = False
sleep = False
child_process_or_thread_count = 4

def run(name:str):
    thread_id = threading.current_thread().native_id
    process_id = os.getpid()
    for i in range(3):
        start = time.time()
        # spinwait
        while (time.time() - start) < 3.0:
            1 + 1
        print(f"{name} count {i} by thread {thread_id}, process {process_id}")
    

if __name__ == "__main__":
    mp.freeze_support()
    pts = []
    for i in range(child_process_or_thread_count):
        if use_threads:
            pts.append(threading.Thread(target=run,args=(f"Thread {i+1}",)))
        else:
            pts.append(mp.Process(target=run,args=(f"Process {i+1}",)))

    start = time.time()
    for pt in pts:
        pt.start()

    for pt in pts:
        pt.join()
    
    duration = time.time() - start
    print(f"Duration {duration}")