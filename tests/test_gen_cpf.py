from pyFBIG import CPFGenerator, CPFProduct

class TestGenCPF:
    def test_factory(self):
        cpf_gen = CPFGenerator()
        factory = cpf_gen.generator_factory()
        assert type(factory) == CPFProduct


    def test_product(self):
        _especil_char: bool = True
        _return_list: bool = False
        _product_len:int
        
        generator = CPFProduct()
        generator.especil_char = _especil_char
        generator.return_list = _return_list
        generator.all_fields = False
        product = generator.gen()
        
        if _especil_char == True and _return_list == False:
            _product_len = 14
        else:
            _product_len = 11
        
        if _return_list == False:
            assert type(product) == str
        else:
            assert type(product) == list
        
        assert len(product) == _product_len
