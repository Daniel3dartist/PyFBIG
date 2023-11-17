from pyFBIG import FakeID

class TestFakeID:
    def test_cpf(self):
        fake = FakeID()
        result = fake.cpf(especial_char=True, return_list=False)
        assert len(result) == 14

    def test_rg(self):
        fake = FakeID()
        result = fake.rg()
        assert type(result) == str
        assert len(result) == 8 or len(result) == 10

if __name__ == "__main__":
    TestFakeID.test_cpf()
    TestFakeID.test_rg()
    