from pyFBIG import RGGenerator, RGProduct

class TestGenRG:
    def test_factory(self):
        rg_gen = RGGenerator()
        factory = rg_gen.generator_factory()
        assert factory.__name__ == RGProduct.__name__


    def test_product(self):# pragma: no cover
        pass


if __name__ == "__main__":
    TestGenRG.test_factory()
    TestGenRG.test_product()