from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Tuple

@dataclass
class Task:
    fn: Callable
    params: Tuple
    cb: Callable 
    at: datetime
    sent: datetime