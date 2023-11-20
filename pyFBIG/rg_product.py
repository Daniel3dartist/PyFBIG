from random import randrange
from .igen_product import IGenProduct
from .BR_names.name import Name

name = Name()

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
            rg = "".join(rg)
        else:
            rg = 'MG'+"".join(rg)

        if self.is_complete == False:
            return rg
        else:
            person = name.gen_name(is_complete=True)
            _name= person['name']
            _gender = person['gender']
            parents = self.parents_creator(_name= _name)
            if parents['father'].split(' ')[0] == _name.split(' ')[0]:
                _list = _name.split(' ')
                _name = _list[0] + ' Junior ' + ' '.join(_list[1:])
            rg_doc: dict = {
                'name':_name,
                'gender': _gender,
                'birth': {
                    'day': self.rand_birthday(),
                    'cite':'Pocos de Caldas',
                    'state':'MG'
                },
                'org': {
                    'name': 'PC',
                    'state': 'MG',
                },
                'affiliation': parents,
                'rg': rg
            }
            return rg_doc
    
    def parents_creator(self, _name) -> dict:
        _list = _name.split(' ')        
        mother = name.gen_female_name()
        father = name.gen_male_name()
        father_midname = name.gen_surname()
        while True:   
            if _list[1] != father_midname and _list[2] != father_midname and mother != _list[0]:
                break
            elif _list[1] != father_midname and _list[2] != father_midname:
                mother = name.gen_female_name()
            else:
                father_midname = name.gen_surname()
        
        mother += ' ' + ' '.join(_list[1:])
        father += ' ' + father_midname + ' ' + _list[-1]

        return {
            'mother': mother,
            'father': father
        }