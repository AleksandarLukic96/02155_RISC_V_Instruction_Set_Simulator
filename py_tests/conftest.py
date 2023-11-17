import pytest
import src.adder as adder

# ADDER
@pytest.fixture(scope='function')
def adder_op_1_test():
    return 12

@pytest.fixture(scope='function')
def adder_op_2_test():
    return 4

@pytest.fixture(scope='function')
def adder_val_in_test():
    return 32

@pytest.fixture(scope='function')
def adder_val_out_test(adder_op_1_test, adder_op_2_test):
    return adder_op_1_test + adder_op_2_test