# Implementation of Immidiate Class and functions 
import signal_constants as const

class Immidiate:
    def __init__(self):
        # inputs
        self.func7 = 0
        self.reg_2 = 0
        self.reg_1 = 0
        self.rd = 0
        self.func3 = 0
        self.opcode = 0

        #Instruction
        self.inst = 0 # <---- Should not be needed!

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

    #Need some help to make sure it identifies the instruction
    # -- The instruction is never parsed.
    # -- The functions should rely on the decoded values.
    # -- Please use the provided get/set methods.
    
    def execute_r_type(self):
        pass

    def execute_i_type(self):
        #Special case for shambi?
        # -- What is shambi?
        # imm_sign = (self.get_inst() >> 31) & 0b1
        # imm_sign_fill = (imm_sign << 19) & 0x1FFFFF
        # imm_11_0 = (self.get_inst() >> 20) & 0b11111111111
        # imm = (imm_sign_fill << 11) | imm_11_0      
        # self.set_res(imm)
        self.set_res((self.get_func7() << 5) | self.get_reg_2())

    def execute_s_type(self):
        # imm_sign = (self.get_inst() >> 31) & 0b1
        # imm_sign_fill = (imm_sign << 19) & 0xFFFFF
        # imm_11_5 = (self.get_inst >> 25) & 0b111111
        # imm_4_0 = (self.get_inst >> 7) & 0b11111
        # imm = imm_sign_fill | imm_11_5 | imm_4_0
        # self.set_res(imm)
        self.set_res((self.get_func7() << 5) | self.get_rd())

    def execute_b_type(self):
        # imm_sign = (self.get_inst() >> 31) & 0b1
        # imm_sign_fill = (imm_sign << 20) & 0x7FFFF
        # imm11 = (self.get_inst() >> 7) & 0b1
        # imm_10_5 = (self.get_inst() >> 20) & 0b111111
        # imm_4_1 = (self.get_inst() >> 7) & 0b1111
        # imm = imm_sign_fill | imm11 | imm_10_5 | imm_4_1 | 0
        # self.set_res(imm)
        
        # func7_6 = (self.get_func7() & 0b1000000) << 5
        # rd_0 = (self.get_rd() & 0b1) << 10
        # func7_5_0 = (self.get_func7() & 0b0111111) << 4
        # rd_4_1 = self.get_rd() >> 1
        # self.set_res((func7_6 | rd_0 | func7_5_0 | rd_4_1) << 1)
        self.set_res((
            ((self.get_func7() & 0b1000000) << 5) 
            | ((self.get_rd() & 0b1) << 10)
            | ((self.get_func7() & 0b0111111) << 4)
            | (self.get_rd() >> 1)
            ) << 1)
        
    def execute_u_type(self):
        imm = self.get_inst & 0xFFFFF000
        self.set_res(imm)
        
    def execute_j_type(self):
        imm20 = (self.get_inst() >> 31) &0b1
        imm11 = (self.get_inst() >> 20) & 0b1
        imm_1_10 = (self.get_inst() >> 21) & 0b1111111111
        imm_19_12 = (self.get_inst() >> 12) & 0b111111111111
        imm = (imm20 << 19) | (imm_19_12 << 11) | (imm11 << 10) | (imm_1_10 << 1) | 0b0
        self.set_res(imm)

    def compute_res(self):
        # Interpret opcode and set immidiate accordingly
        if self.get_opcode() == const.R_TYPE:
            self.execute_r_type()
            
        elif self.get_opcode() == const.I_TYPE:
            self.execute_i_type()
        
        elif self.get_opcode() == const.S_TYPE:
            self.execute_s_type()
        
        elif self.get_opcode() == const.B_TYPE:
            self.execute_b_type()
        
        elif self.get_opcode() == const.U_TYPE_LOAD | const.U_TYPE_ADD:
            self.execute_u_type()
        
        elif self.get_opcode() == const.J_TYPE:
            self.execute_j_type()


if __name__ == "__main__":
    im = Immidiate()
    

    
    val = 0
    im.set_func7(0b0001010)
    im.set_rd(0b00101)
    print(f"func7     : {im.get_func7()}")
    print(f"rd        : {im.get_rd()}")
    
    
