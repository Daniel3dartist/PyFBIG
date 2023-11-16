from abc import ABC, abstractmethod

class IGenerator(ABC):
    """
    Generator Interface Class
    """
    @abstractmethod
    def generate_factory(self):
        pass

    def generate_product(self):
        product = self.generate_factory()
        return product