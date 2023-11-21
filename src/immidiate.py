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
        #Instruction
        self.inst = 0

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
    
    #Instruction
    def set_inst(self, inst):
        self.inst = inst

    def get_inst(self):
        return self.inst
    
    def set_res(self, res):
        self.res = res
    
    def get_res(self):
        return self.res
    
    def compute_res(self):
        pass


#Need some help to make sure it identifies the instruction
    def execute_u_type(self):
        self.res = self.get_inst & 0xFFFFF000
        
    def execute_j_type(self):
        imm20 = (self.get_inst() >> 31) &0b1
        imm11 = (self.get_inst() >> 20) & 0b1
        imm_1_10 = (self.get_inst() >> 21) & 0b1111111111
        imm_19_12 = (self.get_inst() >> 12) & 0b111111111111
        imm = (imm20 << 19) | (imm_19_12 << 11) | (imm11 << 10) | (imm_1_10 << 1) | 0b0
        self.res = imm

    def execute_i_type(self):
        #Special case for shambi?
        imm_sign = (self.get_inst() >> 31) & 0b1
        imm_sign_fill = (imm_sign << 19) & 0x1FFFFF
        imm_11_0 = (self.get_inst() >> 20) & 0b11111111111
        imm = (imm_sign_fill << 11) | imm_11_0
        self.res = imm

    def execute_s_type(self):
        imm_sign = (self.get_inst() >> 31) & 0b1
        imm_sign_fill = (imm_sign << 19) & 0xFFFFF
        imm_11_5 = (self.get_inst >> 25) & 0b111111
        imm_4_0 = (self.get_inst >> 7) & 0b11111
        imm = imm_sign_fill | imm_11_5 | imm_4_0
        self.res = imm

    def execute_b_type(self):
        imm_sign = (self.get_inst() >> 31) & 0b1
        imm_sign_fill = (imm_sign << 20) & 0x7FFFF
        imm11 = (self.get_inst() >> 7) & 0b1
        imm_10_5 = (self.get_inst() >> 20) & 0b111111
        imm_4_1 = (self.get_inst() >> 7) & 0b1111
        imm = imm_sign_fill | imm11 | imm_10_5 | imm_4_1 | 0
        self.res = imm

    #No one for R




