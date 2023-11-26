# Implementation of Adder Class and functions

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
        self.out = self.get_op_1() + self.get_op_2()
    
    def get_out(self):
        return self.out

    def __repr__(self):
        return "op_1: %s, op_2: %s, out: %s" % (self.get_op_1(), self.get_op_2(), self.get_out())
