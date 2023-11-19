import os
import json
from random import randrange
from pyFBIG import Name


path = Name().path

class TestName:
    def rand(self, _len):
        return randrange(0, _len)

    def test_male(self):
        _name = Name()
        result = _name.male_name()
        assert type(result) == list

        with open(path+'/BR_male_names.json') as file:
            json_file = json.load(file)
        _names = json_file['names']
        assert _names == result
        
        _index = self.rand(len(_names))
        assert _names[_index] == result[_index]
    
    def test_female(self):
        _name = Name()
        result = _name.female_name()
        assert type(result) == list

        with open(path+'/BR_female_names.json') as file:
            json_file = json.load(file)
        _names = json_file['names']
        assert _names == result
        
        _index = self.rand(len(_names))
        assert _names[_index] == result[_index]

    def test_surname(self):
        _name = Name()
        result = _name.surname()
        assert type(result) == list

        with open(path+'/BR_surnames.json') as file:
            json_file = json.load(file)
        _surnames = json_file['surnames']
        assert _surnames == result
        
        _index = self.rand(len(_surnames))
        assert _surnames[_index] == result[_index]

    def test_gen_name(self):
        _name = Name()
        result = _name.gen_name(is_complete=False)
        assert type(result) == str
        result = _name.gen_name(is_complete=True)
        assert len(result.split(' ')) == 3 

    def test_gen_male_name(self):
        _name = Name()
        result = _name.gen_male_name()
        assert type(result) == str
    
    def test_gen_female_name(self):
        _name = Name()
        result = _name.gen_female_name()
        assert type(result) == str

    def test_gen_surname(self):
        _name = Name()
        result = _name.gen_surname()
        assert type(result) == str