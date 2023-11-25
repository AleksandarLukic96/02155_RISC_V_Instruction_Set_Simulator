# Implementation of Branch Class and functions
import signal_constants as const

# Branch Class
class Branch:
    def __init__(self):
        # Inputs
        self.op_1 = 0
        self.op_2 = 0
        self.branch_ctrl = 0
        
        # Output
        self.branch_taken = 0
            
    def set_op_1(self, op_1):
        self.op_1 = op_1
    
    def get_op_1(self):
        return self.op_1

    def set_op_2(self, op_2):
        self.op_2 = op_2
    
    def get_op_2(self):
        return self.op_2

    def set_branch_ctrl(self, branch_ctrl):
        self.branch_ctrl = branch_ctrl
    
    def get_branch_ctrl(self):
        return self.branch_ctrl

    def set_branch_taken(self, branch_taken):
        self.branch_taken = branch_taken

    def get_branch_taken(self):
        return self.branch_taken
    
    def branch_taken_enable(self):
        self.branch_taken = 1
    
    def branch_taken_disable(self):
        self.branch_taken = 0
    
    def compute_branch_taken(self):
        if self.get_branch_ctrl() == const.BEQ:
            self.branch_taken_enable() if self.op_1 == self.op_2 else self.branch_taken_disable()

        elif self.get_branch_ctrl() == const.BNE:
            self.branch_taken_enable() if self.op_1 != self.op_2 else self.branch_taken_disable()

        elif self.get_branch_ctrl() == const.BLT:
            if (self.op_1 >> 31 == 1) & (self.op_2 >> 31 == 0):
                self.branch_taken_enable()
            elif (self.op_1 >> 31 == 0) & (self.op_2 >> 31 == 1):
                self.branch_taken_disable()
            else:
                self.branch_taken_enable() if self.op_1 < self.op_2 else self.branch_taken_disable() 
            
        
        elif self.get_branch_ctrl() == const.BGE:
            if (self.op_1 >> 31 == 0) & (self.op_2 >> 31 == 1):
                self.branch_taken_enable()
            elif (self.op_1 >> 31 == 1) & (self.op_2 >> 31 == 0):
                self.branch_taken_disable()
            else:
                self.branch_taken_enable() if self.op_1 >= self.op_2 else self.branch_taken_disable() 
            
        elif self.get_branch_ctrl() == const.BLTU:
            self.branch_taken_enable() if (self.op_1 < self.op_2) else self.branch_taken_disable()
        
        elif self.get_branch_ctrl() == const.BGEU:
            self.branch_taken_enable() if (self.op_1 >= self.op_2) else self.branch_taken_disable()
            
        else:
            pass
    
    def __repr__(self):
        return "op_1: %s, op_2: %s, branch_ctrl: %s, branch_taken: %s" % (self.get_op_1(), self.get_op_2(), self.get_branch_ctrl(), self.get_branch_taken())
        