from threading import Thread
from tkew.task import Task

class Worker:
    def __init__(self):
        self._is_up: bool = False
        self._inflight: Task = None
        self._t: Thread = Thread(target=self._process)

    def _process(self):
        while self._is_up:
            t = self._inflight
            if t is not None:
                res = t.fn(*t.params)
                if t.cb is not None:
                    t.cb(res)
            self._inflight = None
    
    def is_idle(self):
        return self._inflight is None

    def accept(self, t: Task):
        self._inflight = t

    def start(self):
        self._is_up = True
        self._t.start()

    def stop(self):
        self._is_up = False
        self._t.join()