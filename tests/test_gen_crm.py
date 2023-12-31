from pyFBIG import CRMGenerator, CRMProduct



class TestGenCRM:
    def test_factory(self):
        crm_gen = CRMGenerator()
        crm_gen.all_fields = True
        factory = crm_gen.generator_factory()
        assert type(factory) == CRMProduct

    def test_product(self):
        product = CRMProduct()
        product.especial_char = True
        product.return_list = False
        product.all_fields = True
        result = product.gen()
        if product.return_list == True:
            assert type(result) == list
            assert len(result) == 10 
            _str = ''.join(result)
            assert len(_str) == 11
        else:
            assert type(result) == str
            if product.especial_char == True:
                assert len(result) == 13
            else:
                assert len(result) == 11
