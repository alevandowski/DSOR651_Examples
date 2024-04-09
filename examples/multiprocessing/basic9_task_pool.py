'''
    This script demonstrates how a process pool can be used to process a large number of tasks in parallel.
'''

import multiprocessing as mp
import threading
import time
import os

tasks = []
process_count = 2

class TaskPrintHello:

    def __init__(self, postfix="World"):
        self.postfix = postfix

    def run(self):
        print(f"Hello {self.postfix}")


class TaskPrintGoodbye:

    def __init__(self, postfix="World"):
        self.postfix = postfix

    def run(self):
        print(f"Goodbye {self.postfix}")


tasks = [
    TaskPrintHello("John"),
    TaskPrintHello("Jane"),
    TaskPrintHello("Bob"),
    TaskPrintGoodbye("Neil")
]

def run_task(task):
    thread_id = threading.current_thread().native_id
    process_id = os.getpid()
    print(f"Thread {thread_id}, process {process_id} executing task")
    task.run()
    return 1

if __name__ == "__main__":
    mp.freeze_support()

    pool = mp.Pool(process_count)
    start = time.time()
    
    # pool.map passes each element in 2nd iterable argument to the 
    # first argument which specifies a function. The Processes in the Pool
    # execute the first argument for each element in parallel.
    results = pool.map(run_task, tasks)
    print(sum(results))
    duration = time.time() - start
    print(f"Duration {duration}")