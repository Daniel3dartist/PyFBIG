from pyFBIG import FakeID

class TestFakeID:
    def test_cpf(self):
        fake = FakeID()
        result = fake.cpf(especial_char=True, return_list=False)
        assert len(result) == 14


if __name__ == "__main__":
    TestFakeID.test_cpf()
    