from typing import Type
from abc import ABC, abstractmethod
from .igen_product import IGenProduct

class IGenerator(ABC):
    """
    Generator Interface Class
    """
    def __init__(self):
        self.all_fields: bool = True

    @abstractmethod
    def generator_factory(self):
        pass

    def generator(self):
        product: Type[IGenProduct] = self.generator_factory()
        product.all_fields = self.all_fields
        result = product.gen()
        return result