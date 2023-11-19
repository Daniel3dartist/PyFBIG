from .igen_product import IGenProduct

class CRMProduct(IGenProduct):
    def __init__(self):
        self.especial_char: bool = True
        self.return_list: bool = False

    def gen(self):
        _br:str = 'BR'
        crm: list = [str(self.rand_num()) for i in range(0,9)]
        
        if self.return_list == True:
            crm.append(_br)
            return crm
        else:
            if self.especial_char == False:
                return ''.join(crm)+_br
            else:
                _str =  ''.join(crm)
                return str(_str[:-1]+'-'+_str[-1]+"/"+_br)