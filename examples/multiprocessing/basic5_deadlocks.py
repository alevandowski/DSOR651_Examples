'''
    This scripts demonstrates something that you should avoid, a deadlock.
    A deadlock occurs when a process is waiting on another process, and the 
    other process is waiting on another process, such as through a shared lock. 

    The processes become staled waiting for the other, thus the term "deadlock" is used to 
    describe this situation.
'''
import multiprocessing as mp


deadlock_attempt_count = 100


def run1(lock_1, lock_2):
    for i in range(deadlock_attempt_count):
        with lock_1:
            with lock_2:
                print(f"Run1 process acquired both locks for {i+1} time!")

def run2(lock_1, lock_2):
    for i in range(deadlock_attempt_count):
        with lock_2:
            with lock_1:
                print(f"Run2 process acquired both locks for {i+1} time!")


if __name__ == "__main__":
    mp.freeze_support()
    lock_1 = mp.Lock()
    lock_2 = mp.Lock()

    p1 = mp.Process(target=run1,args=(lock_1, lock_2))
    p2 = mp.Process(target=run2,args=(lock_1, lock_2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Sorry, no deadlocks! Try again!")