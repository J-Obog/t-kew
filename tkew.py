from threading import Thread
from multiprocessing import cpu_count
from typing import List, Tuple, Optional

DEFAULT_WORKER_SIZE = cpu_count() // 2 

class TaskQueue:
    def __init__(self, num_workers: int = DEFAULT_WORKER_SIZE):
        self.__workers: List[Thread] = [Thread(target=self.__listen, args=(wid,) ) for wid in range(num_workers)]
        self.__jobs: List[Optional[Tuple]] = [None] * num_workers
        self.__signal: bool = False
    
    def __listen(self, *args, **kwargs):
        wid = args[0]
        while not self.__signal:
            job = self.__jobs[wid] 
            if job != None:
                fn, ags, kwa = job
                fn(*ags, **kwa) 
                self.__jobs[wid] = None

    def __poll(self) -> int:
        i = 0
        n = len(self.__workers)
        while self.__jobs[i % n] != None:
            i += 1
        return i % n

    def start(self):
        for worker in self.__workers:
            worker.start()

    def stop(self):
        while any(self.__jobs):
            pass

        self.__signal = True
        for worker in self.__workers:
            worker.join()

    def queue(self, fn, *args, **kwargs):
        wid = self.__poll()
        self.__jobs[wid] = (fn, args, kwargs)