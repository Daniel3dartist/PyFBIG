from .igen_product import IGenProduct

class CPFProduct(IGenProduct):
    def __init__(self):
        self.especil_char = True
        self.return_list = False


    def gen(self):
        cpf: list = [str(self.rand_num()) for i in range(0, 11)]
        if self.return_list == True:
            return cpf
        else:
            if self.especil_char == False:
                return ''.join(cpf)
            else:
                temp = []
                _from = 0
                _end = 3
                for i in range(0,3):
                    h_dot = '.'
                    if i == 2:
                        h_dot = '-'
                    _str = ''.join(cpf[_from:_end])
                    temp.append(_str+h_dot)
                    _from = _end
                    _end += 3   
                return ''.join(temp) + ''.join(cpf[-2:])
