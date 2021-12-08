from tkew import TaskQueue
import time

def expensive_task(timeout):
    time.sleep(timeout)

def main():
    s = time.perf_counter()
    tq = TaskQueue(1)
    tq.start() 

    tq.queue(expensive_task, 3)

    tq.stop()
    e = time.perf_counter()
    print(f'Program ran in {e - s} seconds')


if __name__ == '__main__':
    main()