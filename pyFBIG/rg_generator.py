from typing import Type
from .igenerator import IGenerator
from .igen_product import IGenProduct
from .rg_product import RGProduct

class RGGenerator(IGenerator):
    def generator_factory(self) -> IGenProduct:
        product: Type[IGenProduct] = RGProduct(all_fields=self.all_fields)
        return product