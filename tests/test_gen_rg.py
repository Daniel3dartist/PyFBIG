from typing import Type
from pyFBIG import RGGenerator, RGProduct

class TestGenRG:
    def test_factory(self):
        rg_gen = RGGenerator()
        product = rg_gen.generate_factory()
        assert product == RGProduct

    def test_gen(self):# pragma:no cover
        pass


if __name__ == "__main__":
    TestGenRG.test_factory()
    TestGenRG.test_gen()