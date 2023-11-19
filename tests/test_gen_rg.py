from pyFBIG import RGGenerator, RGProduct

class TestGenRG:
    def test_factory(self):
        rg_gen = RGGenerator()
        factory = rg_gen.generator_factory()
        assert type(factory) == RGProduct

    def test_product(self):
        product = RGProduct()
        product.is_complete = False
        result = product.gen()
        assert type(result) == str
        if result[:3] == "MG":
            assert len(result[3:]) == 8
        product.is_complete = True
        result = product.gen()
        assert type(result) == dict

if __name__ == "__main__":
    TestGenRG.test_factory()
    TestGenRG.test_product()