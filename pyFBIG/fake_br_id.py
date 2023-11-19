from typing import Type
from .igenerator import IGenerator
from .cpf_generator import CPFGenerator
from .rg_generator import RGGenerator
from .crm_generator import CRMGenerator

class FakeID:
    """
    Fake Brazilian ID generator
    """
    def cpf(self, especial_char: bool = True, return_list: bool = False, is_complete= False):
        """
        CPF (Cadastro de Pessoa Física) generation call function:

        Args:
            especial_char (bool): Defines whether the return will be a string with special characters or just a string containing the generated CPF numbers.
            return_list (bool): Defines whether the return will be a string or a list (the list will always return without special characters). 
        
        Returns:
            Returns the generated CPF numbers. It can return as a string or a list depending on the value of the return_list param is False or True, 
            if it is True the return will be list type if it is False the return will be a string
        """
        cpf_gen: Type[IGenerator] = CPFGenerator()
        cpf_gen.especial_char = especial_char
        cpf_gen.return_list = return_list
        product_result = cpf_gen.generator()
        return product_result
    
    def crm(self, especial_char: bool = True, return_list: bool = False, is_complete= False):
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

    def rg(self, is_complete: bool= False):
        """
        RG (Registro Geral) generation call function:
        Returns:
            Returns the generated RG numbers in string format. 
        """
        rg_gen: Type[IGenerator] = RGGenerator()
        rg_gen.is_complete = is_complete
        product_result = rg_gen.generator()
        return product_result