from .igenerator import IGenerator
from .igen_product import IGenProduct
from .rg_product import RGProduct

class RGGenerator(IGenerator):
    def generator_factory(self) -> IGenProduct:
        return RGProduct()