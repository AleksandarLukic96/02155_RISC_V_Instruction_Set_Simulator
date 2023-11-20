# Implementation of ALU Class and functions
import signal_constants as const

# Function to convert signed to unsigned int
def to_uint32(num):
    return num + 2**32

# ALU Class
class ALU:
    def __init__(self):
        # Inputs
        self.ctrl = 0
        self.op_1 = 0
        self.op_2 = 0
        
        # Output
        self.res = 0
    
    def set_ctrl(self, ctrl):
        self.ctrl = ctrl
    
    def get_ctrl(self):
        return self.ctrl
    
    def set_op_1(self, op_1):
        self.op_1 = op_1
    
    def get_op_1(self):
        return self.op_1

    def set_op_2(self, op_2):
        self.op_2 = op_2
    
    def get_op_2(self):
        return self.op_2
    
    def set_res(self, res):
        self.res = res
    
    def get_res(self):
        return self.res

    def compute_res(self):
        
        if self.get_ctrl() == const.ADD:
            self.set_res(self.op_1 + self.op_2)

        elif self.get_ctrl() == const.SLL:
            self.set_res(self.op_1 << self.op_2)

        elif self.get_ctrl() == const.XOR:
            self.set_res(self.op_1 ^ self.op_2)

        elif self.get_ctrl() == const.OR:
            self.set_res(self.op_1 | self.op_2)

        elif self.get_ctrl() == const.AND:
            self.set_res(self.op_1 & self.op_2)

        elif self.get_ctrl() == const.SRL:
            self.set_res(self.op_1 >> self.op_2)

        elif self.get_ctrl() == const.SUB:
            self.set_res(self.op_1 - self.op_2)                        

        elif self.get_ctrl() == const.SRA:
            self.set_res((self.op_1 >> self.op_2) if (self.op_1 >= 0) else ((self.op_1 + (1 << self.op_2) - 1) >> self.op_2))

        elif self.get_ctrl() == const.SLT: 
            self.set_res(0 | (self.op_1 < self.op_2)) 

        elif self.get_ctrl() == const.SLTU: 
            self.set_res(0 | (to_uint32(self.op_1) < to_uint32(self.op_2)))

        else:
            pass