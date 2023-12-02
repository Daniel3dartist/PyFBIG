from pathlib import Path
from random import randrange
import json

path = Path(__file__).parent.resolve()
path = str(path).replace('\\', '/')
file = open(path+"/states.json", "r", encoding="UTF-8")
j = json.load(file)

class BRStates:
    def __init__(self) -> None:
        self.states = j["states"]

    def get_state(self, state_acronym: str = 'MG') -> dict:
        return self.states[state_acronym]
    
    def rand_state(self) -> dict:
        key_list = [i for i in self.states]
        _key = key_list[(randrange(0, len(key_list)))]
        return self.states[_key]
    
    def rand_city(self, state_acronym: str = 'MG'):
        _file = open(path+f"/{state_acronym}/cities.json", "r", encoding="UTF-8")
        _cities: list = json.load(_file)['cities']
        return _cities[(randrange(0, len(_cities)))]

