from random import randrange
from .igen_product import IGenProduct

class RGProduct(IGenProduct):
    def is_from_minas(self):
        result: int = randrange(1, 11)
        if result == 1:
            return True
        else:
            return False   
    def gen(self):
        rg = [str(self.rand_num()) for i in range(0, 8)]
        if self.is_from_minas() == False:
            return "".join(rg)
        else:
            return 'MG'+"".join(rg)