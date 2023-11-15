# Implementation of ALU Class and functions

# Declare operation constants
ADD  = 0b00000 # 0
SLL  = 0b00001 # 1
XOR  = 0b00100 # 4
OR   = 0b00110 # 6
AND  = 0b00111 # 7
SRL  = 0b00101 # 5
SUB  = 0b01000 # 8
SRA  = 0b01101 # 13
SLT  = 0b00010 # 2
SLTU = 0b00011 # 3

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
    
    def get_res(self):
        return self.res

    def compute_res(self):
        
        if self.get_ctrl() == ADD:
            self.res = self.op_1 + self.op_2

        elif self.get_ctrl() == SLL:
            self.res = self.op_1 << self.op_2

        elif self.get_ctrl() == XOR:
            self.res = self.op_1 ^ self.op_2

        elif self.get_ctrl() == OR:
            self.res = self.op_1 | self.op_2

        elif self.get_ctrl() == AND:
            self.res = self.op_1 & self.op_2

        elif self.get_ctrl() == SRL:
            self.res = self.op_1 >> self.op_2

        elif self.get_ctrl() == SUB:
            self.res = self.op_1 - self.op_2                        

        elif self.get_ctrl() == SRA:
            self.res = (self.op_1 >> self.op_2) if (self.op_1 >= 0) else ((self.op_1 + (1 << self.op_2) - 1) >> self.op_2)

        elif self.get_ctrl() == SLT: 
            self.res = 0 | (self.op_1 < self.op_2) 

        elif self.get_ctrl() == SLTU: 
            self.res = 0 | (self.op_1 < self.op_2)

        else:
            pass