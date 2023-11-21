# Implementation of Adder Class and functions
from ctypes import c_int32

# Function to handle 32-bit overflow
def int32(val):
    return c_int32(val).value

# Adder Class
class Adder:
    def __init__(self, op_1 = 0, op_2 = 0):
        self.op_1 = op_1
        self.op_2 = op_2
        self.out = 0
        
    def set_op_1(self, op_1):
        self.op_1 = op_1
    
    def get_op_1(self):
        return self.op_1
    
    def set_op_2(self, op_2):
        self.op_2 = op_2
    
    def get_op_2(self):
        return self.op_2
    
    def compute_out(self):
        self.out = int32(self.get_op_1() + self.get_op_2())
    
    def get_out(self):
        return self.out

# If file is run as python file, test class functions
if __name__ == "__main__":
    adder = Adder(op_1 = 2, op_2 = 4)
    print(adder.get_out())
    adder.compute_out()
    print(adder.get_out())