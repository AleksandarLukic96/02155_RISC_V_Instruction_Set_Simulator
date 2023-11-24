# Implementation of Immediate Class and functions 
import signal_constants as const
import utils

class Immediate:
    def __init__(self):
        # inputs
        self.func7 = 0
        self.reg_2 = 0
        self.reg_1 = 0
        self.rd = 0
        self.func3 = 0
        self.opcode = 0

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
    
    def execute_r_type(self):
        pass

    def execute_i_type(self):
        self.set_res(utils.sign_extend(
            (self.get_func7() << 5) | self.get_reg_2()
            , msb_pos = 12))

    def execute_s_type(self):
        self.set_res(utils.sign_extend(
            (self.get_func7() << 5) | self.get_rd()
            , msb_pos = 12))

    def execute_b_type(self):
        self.set_res(utils.sign_extend(
            (((self.get_func7() & 0b1000000) << 5)
            | ((self.get_rd() & 0b1) << 10)
            | ((self.get_func7() & 0b0111111) << 4)
            | (self.get_rd() >> 1)
            )
            , msb_pos = 12) << 1) 
        
    def execute_u_type(self):
        self.set_res(
            (self.get_func7() << 25) 
            | (self.get_reg_2() << 20)
            | (self.get_reg_1() << 15)
            | (self.get_func3() << 12)
            )
        
    def execute_j_type(self):
        self.set_res(utils.sign_extend(
            (((self.get_func7() & 0b1000000) << 13)
            | (self.get_reg_1() << 14)
            | (self.get_func3() << 11)
            | ((self.get_reg_2() & 0b00001) << 10)
            | ((self.get_func7() & 0b0111111) << 4)
            | (self.get_reg_2() >> 1)
            )
            , msb_pos = 12) << 1)

    def compute_res(self):
        # Interpret opcode and set immediate according to instruction type
        if self.get_opcode() == const.R_TYPE:
            self.execute_r_type()
            
        elif (self.get_opcode() == const.I_TYPE) | (self.get_opcode() == const.I_TYPE_LOAD) | (self.get_opcode() == const.I_TYPE_JUMP) | (self.get_opcode() == const.I_TYPE_ENV):
            self.execute_i_type()
        
        elif self.get_opcode() == const.S_TYPE:
            self.execute_s_type()
        
        elif self.get_opcode() == const.B_TYPE:
            self.execute_b_type()
        
        elif (self.get_opcode() == const.U_TYPE_LOAD) | (self.get_opcode() == const.U_TYPE_ADD):
            self.execute_u_type()
        
        elif self.get_opcode() == const.J_TYPE:
            self.execute_j_type()
    
    def __repr__(self):
        return "func7: %s, reg_2: %s, reg_1: %s, rd: %s, func3: %s, opcode: %s, res: %s" % (
            self.get_func7(), self.get_reg_2(), self.get_reg_1(), self.get_rd(), self.get_func3(), self.get_opcode(), self.get_res())
