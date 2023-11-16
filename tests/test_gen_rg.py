from typing import Type
from pyFBIG import RGGenerator, RGProduct, IGenProduct

class TestGenRG:
    def test_factory(self):
        rg_gen = RGGenerator()
        product = rg_gen.generate_factory()
        print("Product Type: ", type(product))
        assert type(product) == RGProduct

    def test_gen(self):
        pass


if __name__ == "__main__":
    TestGenRG.test_factory()
    TestGenRG.test_gen()