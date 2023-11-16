from .igenerator import IGenerator
from .igen_product import IGenProduct
from .rg_product import RGProduct

class RGGenerator(IGenerator):
    def generate_factory(self) -> IGenProduct:
        return RGProduct