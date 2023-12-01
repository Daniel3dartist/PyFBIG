from random import randrange
from abc import ABC, abstractmethod

class IGenProduct(ABC):
    def __init__(self, all_fields: bool = True):
        self.all_fields: bool = all_fields

    def rand_num(self) -> int:
        return randrange(0, 9)
    
    def rand_birthday(self) -> str:
        year: int = randrange(1920, 2023)
        month: int = randrange(0, 12)
        month_31days: list = [1,3,5,7,8,10,12]
        day_range: int # Variable that determines the maximum number of days the month will have
        
        if month in month_31days: # Determines the maximum number of days the month will have.
            day_range = 31
        elif month == 2: # Determines if the year is a leap year to adjust the maximum February days
            if type(year/4) == float and type(year/400) == float or type(year/100) == int:
                 day_range = 28
            else:
                 day_range = 29
        else:
            day_range = 30
        day: int = randrange(0, day_range)
        
        birthday: list = [day, month, year]
        for i in range(0, 3):
            index = i-1
            if birthday[index] < 10:
                birthday[index] = '0'+str(birthday[index])
            else:
                 birthday[index] = str(birthday[index])
        return '/'.join(birthday)

    @abstractmethod
    def gen(self):
        pass