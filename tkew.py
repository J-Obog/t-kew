from threading import Thread
from multiprocessing import cpu_count
from typing import List, Tuple, Optional

DEFAULT_WORKER_SIZE = cpu_count() // 2 

class TaskQueue:
    def __init__(self, num_workers: int = DEFAULT_WORKER_SIZE):
        self.__workers: List[Thread] = [Thread(target=None, args=(wid,) ) for wid in range(num_workers)]
        self.__flags: List[Optional[Tuple]] = [None] * num_workers
        self.__signal: bool = True