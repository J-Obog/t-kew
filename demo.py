from tkew import TaskQueue
import time
import random 

def expensive_task(timeout):
    time.sleep(timeout)
    print(f'Finished with {timeout}')


def main():
    s = time.perf_counter()
    tq = TaskQueue(4)
    tq.start() 

    num_tasks = 2
    min_timeout = 1
    max_timeout = 15

    for _ in range(num_tasks): 
        timeout = random.randint(min_timeout, max_timeout)
        tq.queue(expensive_task, timeout)

    tq.stop()
    e = time.perf_counter()
    print(f'Program ran in {e - s} seconds')


if __name__ == '__main__':
    main()