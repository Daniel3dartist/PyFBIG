from typing import Type
from abc import ABC, abstractmethod
from .igen_product import IGenProduct

class IGenerator(ABC):
    """
    Generator Interface Class
    """
    @abstractmethod
    def generator_factory(self):
        pass

    def generator(self):
        product: Type[IGenProduct] = self.generator_factory()
        result = product.gen()
        return result