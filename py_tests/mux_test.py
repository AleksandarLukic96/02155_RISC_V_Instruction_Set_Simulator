import pytest
import src.mux as mux

class Test_MUX2(object):

    mux2 = None

    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.mux2 = mux.Mux2()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.mux2

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, -12), (42, 42)])
    def test_set_in_0(self, input, expected):
        self.mux2.set_in_0(input)
        assert self.mux2.in_0 == expected

    def test_get_in_0(self):
        assert self.mux2.get_in_0() == 0

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, -12), (42, 42)])
    def test_set_in_1(self, input, expected):
        self.mux2.set_in_1(input)
        assert self.mux2.in_1 == expected
        
    def test_get_in_1(self):
        assert self.mux2.get_in_1() == 1

    @pytest.mark.parametrize("in_0, in_1, select, expected", [(0, 0, 0, 0), (0, 12, 0, 0), (12, 0, 0, 12), (0, 42, 1, 42), (8, 0, 1, 0)])
    def test_compute_out(self, in_0, in_1, select, expected):
        self.mux2.in_0 = in_0
        self.mux2.in_1 = in_1
        self.mux2.select = select
        self.mux2.compute_out()
        assert self.mux2.out == expected

    def test_get_out(self):
        assert self.mux2.get_out() == 0

class Test_MUX3(object):

    mux3 = mux.Mux3()

    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.mux3 = mux.Mux3()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.mux3

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, -12), (42, 42)])
    def test_set_in_0(self, input, expected):
        self.mux3.set_in_0(input)
        assert self.mux3.in_0 == expected

    def test_get_in_0(self):
        assert self.mux3.get_in_0() == 0

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, -12), (42, 42)])
    def test_set_in_1(self, input, expected):
        self.mux3.set_in_1(input)
        assert self.mux3.in_1 == expected
        
    def test_get_in_1(self):
        assert self.mux3.get_in_1() == 1

    @pytest.mark.parametrize("input, expected", [(0, 0), (1, 1), (-12, -12), (42, 42)])
    def test_set_in_2(self, input, expected):
        self.mux3.set_in_2(input)
        assert self.mux3.in_2 == expected

    def test_get_in_2(self):
        assert self.mux3.get_in_2() == 2
    
    @pytest.mark.parametrize("in_0, in_1, in_2, select, expected", [(0, 0, 0, 0, 0), (0, 12, 23, 0, 0), (12, 0, 17, 0, 12), (0, 42, 13, 1, 42), (8, 5, 66, 1, 5), (2, 5, 66, 2, 66)])
    def test_compute_out(self, in_0, in_1, in_2, select, expected):
        self.mux3.in_0 = in_0
        self.mux3.in_1 = in_1
        self.mux3.in_2 = in_2
        self.mux3.select = select
        self.mux3.compute_out()
        assert self.mux3.out == expected

    def test_get_out(self):
        assert self.mux3.get_out() == 0
            