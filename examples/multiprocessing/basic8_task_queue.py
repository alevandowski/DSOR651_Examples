'''
    This script demonstrates the use of queues to communicate data between processes.
'''
import multiprocessing as mp
import time

queue = mp.Queue()
child_process_or_thread_count = 2

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

queue.put(TaskPrintHello("John"))
queue.put(TaskPrintHello("Jane"))
queue.put(TaskPrintHello("Bob"))
queue.put(TaskPrintGoodbye("Neil"))

def run_task(name,queue:mp.Queue):

    while True:
        task = queue.get()

        print(f"{name} executing {task}")
        if task is None:
            break
        else:
            task.run()

if __name__ == "__main__":
    mp.freeze_support()
    pts = []
    for i in range(child_process_or_thread_count):
        pts.append(mp.Process(target=run_task,args=(f"Process {i+1}",queue)))

    start = time.time()
    for pt in pts:
        pt.start()
    queue.put(TaskPrintGoodbye("Class"))
    # 

    for i in range(child_process_or_thread_count):
        queue.put(None)
    for pt in pts:
        pt.join()
    
    duration = time.time() - start
    print(f"Duration {duration}")