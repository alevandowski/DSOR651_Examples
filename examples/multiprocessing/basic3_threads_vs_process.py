'''
 This examples demonstrates that threads can share memory and child processes, by default, do not. 

 Notice the global_list is a mutable list that is created in the root process/thread.

 If the child thread shares memory with the root process, then the global_list gets updated
 otherwise, it doesn't.   The root_thread prints out the values of the global_list at the end. 
'''
import multiprocessing as mp
import threading

use_threads = False
child_process_or_thread_count = 4
global_list = []

def run(name:str):
    for i in range(10):
        global_list.append(f"{name} counting to {i}")

if __name__ == "__main__":
    mp.freeze_support()
    pts = []
    for i in range(child_process_or_thread_count):
        if use_threads:
            pts.append(threading.Thread(target=run,args=(f"Thread {i+1}",)))
        else:
            pts.append(mp.Process(target=run,args=(f"Process {i+1}",)))

    for pt in pts:
        pt.start()

    for pt in pts:
        pt.join()
    
    print(global_list)