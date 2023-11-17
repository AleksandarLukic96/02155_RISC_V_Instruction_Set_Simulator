import pytest
import src.adder as adder

class Test_Adder(object):
    
    adder = adder.Adder()
    
    @pytest.fixture(autouse=True)
    def setup_class(self, adder_op_1_test, adder_op_2_test):
        print(f"Setting up {self}")
        self.adder = adder.Adder(adder_op_1_test, adder_op_2_test)
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.adder

    def test_set_op_1(self, adder_val_in_test):
        self.adder.set_op_1(adder_val_in_test)
        assert self.adder.op_1 == adder_val_in_test

    def test_get_op_1(self, adder_op_1_test):
        assert self.adder.get_op_1() == adder_op_1_test

    def test_set_op_2(self, adder_val_in_test):
        self.adder.set_op_2(adder_val_in_test)
        assert self.adder.op_2 == adder_val_in_test
        
    def test_get_op_2(self, adder_op_2_test):
        assert self.adder.get_op_2() == adder_op_2_test

    def test_compute_out(self, adder_val_out_test):
        self.adder.compute_out()
        assert self.adder.out == adder_val_out_test
                
    def test_get_out(self):
        assert self.adder.get_out() == 0
