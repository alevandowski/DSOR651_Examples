'''
This script demonstrates a Lock.  Locks are a form of communication between processes. 
Processes can use them to ensure a resource or a piece of code is not executed simultaneously.

Generally code is written with Locks to control with Process has access to a resource or which Process should execute a piece of code.

If a lock is taken, the process often waits until a lock is released for another process to execute.

'''
import multiprocessing as mp
import threading
import os
import time

use_threads = False
child_process_or_thread_count = 4
write_to_console_lock = mp.Lock()

def run(name, write_to_console_lock):
    with write_to_console_lock:
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
            pts.append(threading.Thread(target=run,args=(f"Thread {i+1}",write_to_console_lock)))
        else:
            pts.append(mp.Process(target=run,args=(f"Process {i+1}",write_to_console_lock)))

    for pt in pts:
        pt.start()

    for pt in pts:
        pt.join()
