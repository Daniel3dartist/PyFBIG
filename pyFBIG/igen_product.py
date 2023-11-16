from abc import ABC, abstractmethod

class IGenProduct(ABC):
    @abstractmethod
    def gen(self):
        pass