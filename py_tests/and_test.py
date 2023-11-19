import pytest
import src.and_ as and_

class Test_AND(object):

    and_ = None

    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.and_ = and_.AND()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.and_

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, 1), (42, 1)])
    def test_set_in_0(self, input, expected):
        self.and_.set_in_0(input)
        assert self.and_.in_0 == expected

    def test_get_in_0(self):
        assert self.and_.get_in_0() == 0

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, 1), (42, 1)])
    def test_set_in_1(self, input, expected):
        self.and_.set_in_1(input)
        assert self.and_.in_1 == expected
        
    def test_get_in_1(self):
        assert self.and_.get_in_1() == 0

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, 1), (42, 1)])
    def test_set_out(self, input, expected):
        self.and_.set_out(input)
        assert self.and_.out == expected
        
    def test_get_out(self):
        assert self.and_.get_out() == 0
            
    @pytest.mark.parametrize("in_0, in_1, expected", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)])
    def test_compute_out(self, in_0, in_1, expected):
        self.and_.in_0 = in_0
        self.and_.in_1 = in_1
        self.and_.compute_out()
        assert self.and_.out == expected

