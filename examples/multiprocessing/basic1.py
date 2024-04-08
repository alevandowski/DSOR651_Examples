'''
    A hello-world example that is printed to the console in a child process.
'''
import multiprocessing as mp


def run():
    print("Hello World")

if __name__ == "__main__":
    mp.freeze_support()
    p1 = mp.Process(target=run)

    p1.start()
    p1.join()