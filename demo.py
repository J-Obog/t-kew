from tkew import TaskQueue
import time
import random 

def expensive_task(timeout):
    time.sleep(timeout)
    print(f'Finished with {timeout}')


def main():
    s = time.perf_counter()
    tq = TaskQueue(5)
    tq.start() 

    num_taks = 10
    min_timeout = 1
    max_timeout = 15
    sm = 0

    for _ in range(num_taks): 
        timeout = random.randint(min_timeout, max_timeout)
        sm += timeout
        tq.queue(expensive_task, timeout)

    print(sm)

    tq.stop()
    e = time.perf_counter()
    print(f'Program ran in {e - s} seconds')


if __name__ == '__main__':
    main()