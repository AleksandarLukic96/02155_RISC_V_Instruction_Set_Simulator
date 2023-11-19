import pytest
import src.adder as adder

class Test_Adder(object):
    
    adder = None
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.adder = adder.Adder()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.adder

    @pytest.mark.parametrize("val, expected", [(0, 0), (1, 1), (42, 42)])
    def test_set_op_1(self, val, expected):
        self.adder.set_op_1(val)
        assert self.adder.op_1 == expected

    def test_get_op_1(self):
        assert self.adder.get_op_1() == 0

    @pytest.mark.parametrize("val, expected", [(0, 0), (1, 1), (42, 42)])
    def test_set_op_2(self, val, expected):
        self.adder.set_op_2(val)
        assert self.adder.op_2 == expected
        
    def test_get_op_2(self):
        assert self.adder.get_op_2() == 0

    @pytest.mark.parametrize("op_1, op_2, expected", [(0, 0, 0), (0, 1, 1), (-1, 0, -1), (0x7FFFFFFF, 0x00000000, 0x7FFFFFFF), (0xFFFFFFFF, 0x00000001, 0x00000000)])
    def test_compute_out(self, op_1, op_2, expected):
        self.adder.op_1 = op_1
        self.adder.op_2 = op_2
        self.adder.compute_out()
        assert self.adder.out == expected
                
    def test_get_out(self):
        assert self.adder.get_out() == 0
