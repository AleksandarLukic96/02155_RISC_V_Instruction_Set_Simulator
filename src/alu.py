# Implementation of ALU Class and functions

# Function to convert signed to unsigned int
def to_uint32(num):
    return num + 2**32

# Declare operation constants
# R-type
ADD   = 'ADD'   # 0b00000 # 0
SUB   = 'SUB'   # 0b01000 # 8
XOR   = 'XOR'   # 0b00100 # 4
OR    = 'OR'    # 0b00110 # 6
AND   = 'AND'   # 0b00111 # 7
SLL   = 'SLL'   # 0b00001 # 1
SRL   = 'SRL'   # 0b00101 # 5
SRA   = 'SRA'   # 0b01101 # 13
SLT   = 'SLT'   # 0b00010 # 2
SLTU  = 'SLTU'  # 0b00011 # 3

# I-type
ADDI  = 'ADDI'  # 0b00000 # 0
XORI  = 'XORI'  # 0b00100 # 4
ORI   = 'ORI'   # 0b00110 # 6
ANDI  = 'ANDI'  # 0b00111 # 7
SLLI  = 'SLLI'  # 0b00001 # 1
SRLI  = 'SRLI'  # 0b00101 # 5
SRAI  = 'SRAI'  # 0b00101 # 5
SLTI  = 'SLTI'  # 0b00010 # 2
SLTIU = 'SLTIU' # 0b00011 # 3

# I-type load
LB    = 'LB'    # 0b00000 # 0
LH    = 'LH'    # 0b00001 # 1
LW    = 'LW'    # 0b00010 # 2
LBU   = 'LBU'   # 0b00100 # 4
LHU   = 'LHU'   # 0b00101 # 5

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
        
        if self.get_ctrl() == ADD:
            self.set_res(self.op_1 + self.op_2)

        elif self.get_ctrl() == SLL:
            self.set_res(self.op_1 << self.op_2)

        elif self.get_ctrl() == XOR:
            self.set_res(self.op_1 ^ self.op_2)

        elif self.get_ctrl() == OR:
            self.set_res(self.op_1 | self.op_2)

        elif self.get_ctrl() == AND:
            self.set_res(self.op_1 & self.op_2)

        elif self.get_ctrl() == SRL:
            self.set_res(self.op_1 >> self.op_2)

        elif self.get_ctrl() == SUB:
            self.set_res(self.op_1 - self.op_2)                        

        elif self.get_ctrl() == SRA:
            self.set_res((self.op_1 >> self.op_2) if (self.op_1 >= 0) else ((self.op_1 + (1 << self.op_2) - 1) >> self.op_2))

        elif self.get_ctrl() == SLT: 
            self.set_res(0 | (self.op_1 < self.op_2)) 

        elif self.get_ctrl() == SLTU: 
            self.set_res(0 | (to_uint32(self.op_1) < to_uint32(self.op_2)))

        else:
            pass