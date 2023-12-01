from .igen_product import IGenProduct

class CPFProduct(IGenProduct):
    def __init__(self):
        self.especil_char: bool = True
        self.return_list: bool = False
        self.all_fields: bool = True

    def gen(self):
        cpf: list = [str(self.rand_num()) for i in range(0, 11)]
        result = cpf
        if self.return_list == True:
            return result
        else:
            if self.especil_char == False:
                result = ''.join(cpf)
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
                result =  ''.join(temp) + ''.join(cpf[-2:])
        
        if self.all_fields == False:
            return result
        else:
            # TODO - Need add person info (first name, surname, parents, etc.)
            return {'cpf': result}