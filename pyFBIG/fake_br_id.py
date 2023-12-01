from typing import Type
from .igenerator import IGenerator
from .cpf_generator import CPFGenerator
from .rg_generator import RGGenerator
from .crm_generator import CRMGenerator

class FakeID:
    """
    Fake Brazilian ID generator
    """
    def cpf(self, especial_char: bool = True, return_list: bool = False):
        """
        CPF (Cadastro de Pessoa Física) generation call function:

        Args:
            especial_char (bool): Defines whether the return will be a string with special characters or just a string containing the generated CPF numbers.
            return_list (bool): Defines whether the return will be a string or a list (the list will always return without special characters). 
        
        Returns:
            Returns the generated CPF numbers and person data (the first name, surname, etc.). It return a dictionary.
        """
        cpf_gen: Type[IGenerator] = CPFGenerator()
        cpf_gen.especial_char = especial_char
        cpf_gen.return_list = return_list
        cpf_gen.all_fields = True
        product_result = cpf_gen.generator()
        return product_result

    def cpf_number(self, especial_char: bool = True, return_list: bool = False):
        """
        CPF (Cadastro de Pessoa Física) generation call function:

        Args:
            especial_char (bool): Defines whether the return will be a string with special characters or just a string containing the generated CPF numbers.
            return_list (bool): Defines whether the return will be a string or a list (the list will always return without special characters). 
        
        Returns:
            Returns the generated CPF numbers. It return a string.
        """
        cpf_gen: Type[IGenerator] = CPFGenerator()
        cpf_gen.especial_char = especial_char
        cpf_gen.return_list = return_list
        cpf_gen.all_fields = False
        product_result = cpf_gen.generator()
        return product_result

    def crm(self, especial_char: bool = True, return_list: bool = False):
        """
        CRM (Conselho Regional de Medicina) generation call function:

        Args:
            especial_char (bool): Defines whether the return will be a string with special characters or just a string containing the generated CPF numbers.
            return_list (bool): Defines whether the return will be a string or a list (the list will always return without special characters). 
        
        Returns:
            Returns the generated CRM numbers. It can return as a string or a list depending on the value of the return_list param is False or True, 
            if it is True the return will be list type if it is False the return will be a string
        """
        crm_gen: Type[IGenerator] = CRMGenerator()
        crm_gen.especial_char = especial_char
        crm_gen.return_list = return_list
        product_result = crm_gen.generator()
        return product_result

    def crm_number(self, especial_char: bool = True, return_list: bool = False):
        """
        CRM (Conselho Regional de Medicina) generation call function:

        Args:
            especial_char (bool): Defines whether the return will be a string with special characters or just a string containing the generated CPF numbers.
            return_list (bool): Defines whether the return will be a string or a list (the list will always return without special characters). 
        
        Returns:
            Returns the generated CRM numbers. It can return as a string or a list depending on the value of the return_list param is False or True, 
            if it is True the return will be list type if it is False the return will be a string
        """
        crm_gen: Type[IGenerator] = CRMGenerator()
        crm_gen.especial_char = especial_char
        crm_gen.return_list = return_list
        product_result = crm_gen.generator()
        return product_result

    def rg(self):
        """
        RG (Registro Geral) generation call function:
        
        Args:
            is_complete: Defines whether it will return a simple string containing just an RG number or 
            whether it will return a dictionary containing all information present in an RG

        Returns:
            Returns the generated RG number and person data (the first name, surname, city, state, birthday, etc.). It return a dictionary. 
        """
        rg_gen: Type[IGenerator] = RGGenerator()
        rg_gen.all_fields = True
        product_result = rg_gen.generator()
        return product_result

    def rg_number(self):
        """
        RG (Registro Geral) generation call function:
        
        Args:
            is_complete: Defines whether it will return a simple string containing just an RG number or 
            whether it will return a dictionary containing all information present in an RG

        Returns:
            Returns the generated RG fake data. It return a string. 
        """
        rg_gen: Type[IGenerator] = RGGenerator()
        rg_gen.all_fields= False
        product_result = rg_gen.generator()
        return product_result