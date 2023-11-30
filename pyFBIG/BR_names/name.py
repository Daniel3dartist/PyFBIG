import json
import os
from pathlib import Path
from random import randrange

path = Path(__file__).parent.resolve()
path = str(path).replace('\\', '/')

class Name:
    def __init__(self):
        self.path = path

    def json_load(self, name_list):
        return json.load(name_list)

    def female_name(self):
        female_name = open(path + '/BR_female_names.json')
        _list = self.json_load(name_list=female_name) 
        return _list['names']

    def male_name(self):
        male_name = open(path + '/BR_male_names.json')
        _list = self.json_load(name_list=male_name) 
        return _list['names']
    
    def surname(self):
        male_name = open(path + '/BR_surnames.json')
        _list = self.json_load(name_list=male_name) 
        return _list['surnames']
    
    def gen_name(self, is_complete: bool = False):
        rand_list: list = [self.gen_female_name(), self.gen_male_name()]
        _index = randrange(0, 2)
        gender: str = "M"
        _name = rand_list[_index] 
        if _index < 1:
            gender = 'F'
        if is_complete == False:
            return _name
        else:
            surnames: list = [self.gen_surname()]
            while True:
                if len(surnames) == 2:
                    break
                rand_surname: str = self.gen_surname()
                if surnames[0] != rand_surname:
                    surnames.append(rand_surname)
            return {'name': _name + ' '+ surnames[0] + ' ' + surnames[1], 'gender': gender}
    
    def gen_female_name(self):
        female_name = self.female_name()
        return female_name[randrange(0, len(female_name))]

    def gen_male_name(self):
        male_name = self.male_name()
        return male_name[randrange(0, len(male_name))]

    def gen_surname(self):
        surname = self.surname()
        return surname[randrange(0, len(surname))]


if __name__ == "__main__":
    Name().female_name()
    Name().male_name()
    Name().surname()