from pyFBIG.BR_states import BRStates 

brs = BRStates()

class TestBRStates:
    def test_rand_state(self):
        assert type(brs.rand_state()) == dict