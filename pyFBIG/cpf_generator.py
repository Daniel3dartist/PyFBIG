from typing import Type
from .igenerator import IGenerator
from .igen_product import IGenProduct
from .cpf_product import CPFProduct

class CPFGenerator(IGenerator):
    def __init__(self):
        self.especial_char: bool = True
        self.return_list: bool = False
        self.all_fields: bool = True

    def generator_factory(self) -> IGenProduct:
        product: Type[IGenProduct] = CPFProduct()
        product.especil_char = self.especial_char
        product.return_list = self.return_list
        return product