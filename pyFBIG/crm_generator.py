from typing import Type
from .igenerator import IGenerator
from .igen_product import IGenProduct
from .crm_product import CRMProduct

class CRMGenerator(IGenerator):
    def __init__(self):
        self.especial_char: bool = True
        self.return_list: bool = False
    
    def generator_factory(self) -> IGenProduct:
        product: Type[IGenProduct] = CRMProduct()
        product.especial_char = self.especial_char
        product.return_list = self.return_list
        return product