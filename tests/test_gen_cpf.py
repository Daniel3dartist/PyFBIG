from pyFBIG import CPFGenerator, CPFProduct, IGenProduct

class TestGenCPF:
    def test_factory(self):
        cpf_gen = CPFGenerator()
        product = cpf_gen.generate_factory()
        assert type(product) == CPFProduct

    def test_gen(self):
        pass


if __name__ == "__main__":
    TestGenCPF.test_factory()
    TestGenCPF.test_gen()