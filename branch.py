# Implementation of Branch Class and functions

# Function to convert signed to unsigned int
def to_uint32(num):
    return num + 2**32

# Declare branch constants
BEQ  = 0b00000 # 0
BNE  = 0b00001 # 1
BLT  = 0b00100 # 4
BGE  = 0b00101 # 5
BLTU = 0b00110 # 6
BGEU = 0b00111 # 7

# Branch Class
class Branch:
    def __init__(self):
        # Inputs
        self.op_1 = 0
        self.op_2 = 0
        self.branch_ctrl = 0
        
        # Output
        self.branch_taken = 0
        
    def set_branch_ctrl(self, branch_ctrl):
        self.branch_ctrl = branch_ctrl
    
    def get_branch_ctrl(self):
        return self.branch_ctrl
    
    def set_op_1(self, op_1):
        self.op_1 = op_1
    
    def get_op_1(self):
        return self.op_1

    def set_op_2(self, op_2):
        self.op_2 = op_2
    
    def get_op_2(self):
        return self.op_2

    def branch_taken_enable(self):
        self.branch_taken = 1
    
    def branch_taken_disable(self):
        self.branch_taken = 0
    
    def compute_branch_taken(self):
        if self.get_branch_ctrl() == BEQ:
            self.branch_taken_enable() if self.op_1 == self.op_2 else self.branch_taken_disable()

        elif self.get_branch_ctrl() == BNE:
            self.branch_taken_enable() if self.op_1 != self.op_2 else self.branch_taken_disable()

        elif self.get_branch_ctrl() == BLT:
            self.branch_taken_enable() if self.op_1 < self.op_2 else self.branch_taken_disable()
        
        elif self.get_branch_ctrl() == BGE:
            self.branch_taken_enable() if self.op_1 >= self.op_2 else self.branch_taken_disable()
        
        elif self.get_branch_ctrl() == BLTU:
            self.branch_taken_enable() if to_uint32(self.op_1) < to_uint32(self.op_2) else self.branch_taken_disable()
        
        elif self.get_branch_ctrl() == BGEU:
            self.branch_taken_enable() if to_uint32(self.op_1) >= to_uint32(self.op_2) else self.branch_taken_disable()
            
        else:
            pass
