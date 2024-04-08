'''
This script demonstrates a Semaphore.  Semaphore are a form of communication
between processes. 
Processes can use semaphores to ensure a resource or a piece of code is not
executed simultaneously or up to a value specifed by a semaphore.

For example, if you want a section of code to be only executed by two processes
at point in time, you can create and use aSemaphore(2) to control this.
'''
import multiprocessing as mp
import threading
import os
import time

use_threads = False
child_process_or_thread_count = 4
write_to_console_semaphore = mp.Semaphore(3)

def run(name, write_to_console_semaphore):
    with write_to_console_semaphore:
        thread_id = threading.current_thread().native_id
        process_id = os.getpid()
        time.sleep(3)
     
        for i in range(10):
            #if sleep:
            #   time.sleep(1) 
            print(f"{name} count {i} by thread {thread_id}, process {process_id}")
            
            
if __name__ == "__main__":
    mp.freeze_support()
    pts = []
    for i in range(child_process_or_thread_count):
        if use_threads:
            pts.append(threading.Thread(target=run,args=(f"Thread {i+1}",write_to_console_semaphore)))
        else:
            pts.append(mp.Process(target=run,args=(f"Process {i+1}",write_to_console_semaphore)))

    start = time.time()
    for pt in pts:
        pt.start()

    for pt in pts:
        pt.join()
    duration = time.time() - start

    print(f"Duration {duration}")
