# Implementation of Decoder Class and functions 

# Decoder Class
class Decoder:
    def __init__(self):
        self.inst = 0
        self.opcode = 0
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0
        
    def set_inst(self, inst_in):
        self.inst = inst_in

    def get_inst(self):
        return self.inst
    
    def set_opcode(self):
        self.opcode = self.inst & 0b1111111    
    
    def get_opcode(self):
        return self.opcode    

    def set_reg_1(self):
        self.reg_1 = (self.inst >> 15) & 0b11111    
    
    def get_reg_1(self):
        return self.reg_1    

    def set_reg_2(self):
        self.reg_2 = (self.inst >> 20) & 0b11111    
    
    def get_reg_2(self):
        return self.reg_2    

    def set_rd(self):
        self.rd = (self.inst >> 7) & 0b11111    
    
    def get_rd(self):
        return self.rd    
