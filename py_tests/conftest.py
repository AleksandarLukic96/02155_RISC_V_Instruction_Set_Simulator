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

# BRANCH constants
@pytest.fixture(scope='function')
def BEQ():
    return 0b00000 # 0
 
@pytest.fixture(scope='function')
def BNE():
    return 0b00001 # 1

@pytest.fixture(scope='function')
def BLT():
    return 0b00100 # 4

@pytest.fixture(scope='function')
def BGE():
    return 0b00101 # 5

@pytest.fixture(scope='function')
def BLTU():
    return 0b00110 # 6

@pytest.fixture(scope='function')
def BGEU():
    return 0b00111 # 7
