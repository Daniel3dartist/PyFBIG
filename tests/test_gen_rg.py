from pyFBIG import RGGenerator, RGProduct

class TestGenRG:
    def test_factory(self):
        rg_gen = RGGenerator()
        factory = rg_gen.generator_factory()
        assert type(factory) == RGProduct

    def test_product(self):
        product = RGProduct(all_fields=False)
        result = product.gen()
        assert type(result) == str
        if result[:3] == "MG":
            assert len(result[3:]) == 8
        product= RGProduct(all_fields=True)
        result = product.gen()
        assert type(result) == dict
        birthday = result['birth']['day']
        assert type(birthday) == str
        list_birthday = birthday.split('/')
        assert len(list_birthday) == 3
        assert len(list_birthday[0]) == 2 and len(list_birthday[1]) == 2 and len(list_birthday[2]) == 4

if __name__ == "__main__":
    TestGenRG.test_factory()
    TestGenRG.test_product()