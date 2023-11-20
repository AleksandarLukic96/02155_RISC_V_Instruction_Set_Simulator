# Implementation of Decoder Class and functions 

# Decoder Class
class Decoder:
    def __init__(self):
        self.inst = 0
        self.opcode = 0
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0
        
    def set_inst(self, inst):
        self.inst = inst

    def get_inst(self):
        return self.inst

    def set_opcode(self, opcode):
        self.opcode = opcode

    def get_opcode(self):
        return self.opcode

    def set_reg_1(self, reg_1):
        self.reg_1 = reg_1
    
    def get_reg_1(self):
        return self.reg_1

    def set_reg_2(self, reg_2):
        self.reg_2 = reg_2

    def get_reg_2(self):
        return self.reg_2

    def set_rd(self, rd):
        self.rd = rd
    
    def get_rd(self):
        return self.rd

    def compute_decoding(self):
        self.set_opcode(self.inst & 0b1111111)
        self.set_reg_1((self.inst >> 15) & 0b11111)
        self.set_reg_2((self.inst >> 20) & 0b11111)
        self.set_rd((self.inst >> 7) & 0b11111)
