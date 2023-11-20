# Implementation of Immidiate Class and functions 

class Immidiate:
    def __init__(self):
        # inputs
        self.opcode = 0
        self.func3 = 0
        self.func7 = 0
        self.rd = 0
        self.reg_1 = 0
        self.reg_2 = 0

        # Output
        self.res = 0

    def set_opcode(self, opcode):
        self.opcode = opcode

    def get_opcode(self):
        return self.opcode

    def set_func3(self, func3):
        self.func3 = func3

    def get_func3(self):
        return self.func3
    
    def set_func7(self, func7):
        self.func7 = func7

    def get_func7(self):
        return self.func7

    def set_rd(self, rd):
        self.rd = rd

    def get_rd(self):
        return self.rd

    def set_reg_1(self, reg_1):
        self.reg_1 = reg_1

    def get_reg_1(self):
        return self.reg_1
    
    def set_reg_2(self, reg_2):
        self.reg_2 = reg_2
    
    def get_reg_2(self):
        return self.reg_2
    
    def set_res(self, res):
        self.res = res
    
    def get_res(self):
        return self.res
    
    def compute_res(self):
        pass
