from tkew import TaskQueue
from time import sleep

def expensive_task(timeout):
    sleep(timeout)

def main():
    tq = TaskQueue(1)
    tq.start() 

    tq.queue(expensive_task, 3)

    tq.stop()


if __name__ == '__main__':
    main()