from random import randrange
from abc import ABC, abstractmethod

class IGenProduct(ABC):
    def __init__(self):
        self.is_complete = False

    def rand_num(self) -> int:
        return randrange(0, 9)
    
    @abstractmethod
    def gen(self):
        pass