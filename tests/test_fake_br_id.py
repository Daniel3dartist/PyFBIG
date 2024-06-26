from pyFBIG import FakeID

class TestFakeID:
    def test_cpf(self):
        fake = FakeID()
        result = fake.cpf(especial_char=True, return_list=False)
        assert type(result) == dict
    
    def test_cpf_number(self):
        fake = FakeID()
        result = fake.cpf_number(especial_char=True, return_list=False)
        assert len(result) == 14

    def test_rg(self):
        fake = FakeID()
        result = fake.rg()
        assert type(result) == dict
        name = result['name'].split(' ')
        mother = result['affiliation']['mother'].split(' ')
        assert len(mother) == 3
        father = result['affiliation']['father'].split(' ')
        assert len(father) == 3
        assert mother[-1] == father[-1] and mother[1] != father[1]
        assert mother[0] != name[0]
        if name[1] == 'Junior':
            assert len(name) == 4
            assert name[2] == mother[1] and name[-1] == father[-1]
        else:
            assert len(name) == 3
            assert name[1] == mother[1] and name[-1] == father[-1]

    def test_rg_number(self):
        fake = FakeID()
        result = fake.rg_number()
        assert type(result) == str
        assert len(result) == 8 or len(result) == 10

    def test_crm_number(self):
        fake = FakeID()
        result = fake.crm_number(especial_char=True, return_list=False)
        assert len(result) == 13

    def test_crm(self):
        fake = FakeID()
        result = fake.crm()
        assert result != None
    