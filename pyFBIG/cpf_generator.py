from .igenerator import IGenerator
from .igen_product import IGenProduct
from .cpf_product import CPFProduct

class CPFGenerator(IGenerator):
    def generate_factory(self) -> IGenProduct:
        return CPFProduct()