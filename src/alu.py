# Implementation of ALU Class and functions
import signal_constants as const
import utils

# Function to convert signed to unsigned int
def to_uint32(num):
    return num + 2**32

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
        
    # R-type operations
    def compute_add(self): 
        self.set_res(utils.remove_overflow(
            self.op_1 + self.op_2)
        )

    def compute_sub(self):
        self.set_res(utils.remove_overflow(
            self.op_1 - self.op_2)
        )
    
    def compute_xor(self):
        self.set_res(self.op_1 ^ self.op_2)
    
    def compute_or(self):
        self.set_res(self.op_1 | self.op_2)
    
    def compute_and(self):
        self.set_res(self.op_1 & self.op_2)
    
    def compute_sll(self):
        self.set_res(utils.remove_overflow(
            self.op_1 << (self.op_2 & 0x0000001F))
        )
    
    def compute_srl(self):
        self.set_res(self.op_1 >> (self.op_2 & 0x0000001F))
    
    def compute_sra(self):
        shift_by_value = self.op_2 & 0x0000001F
        shifted_val = self.op_1 >> shift_by_value 
        msb_pos_shifted = 32 - shift_by_value
        exteded_val = utils.sign_extend(shifted_val, msb_pos = msb_pos_shifted)
        self.set_res(exteded_val)
    
    def compute_slt(self):
        if (self.op_1 >> 31 == 1) & (self.op_2 >> 31 == 0):
            res = 1
        elif (self.op_1 >> 31 == 0) & (self.op_2 >> 31 == 1):
            res = 0
        else:
            res = (0 | (self.op_1 < self.op_2))
        self.set_res(res) 
    
    def compute_sltu(self):
        self.set_res(0 | (self.op_1 < self.op_2))
    
    # I-type operations
    def compute_addi(self):
        self.compute_add()
    
    def compute_xori(self):
        self.compute_xor()
    
    def compute_ori(self):
        self.compute_or()
    
    def compute_andi(self):
        self.compute_and()
    
    def compute_slli(self):
        self.compute_sll()
    
    def compute_srli(self):
        self.compute_srl()
    
    def compute_srai(self):
        self.compute_sra()
    
    def compute_slti(self):
        self.compute_slt()
    
    def compute_sltiu(self):
        self.compute_sltu()
    
    # I-type load
    def compute_lb(self):
        pass
    
    def compute_lh(self):
        pass
    
    def compute_lw(self):
        pass
    
    def compute_lbu(self):
        pass
    
    def compute_lhu(self):
        pass
    
    # S-type
    def compute_sb(self):
        pass
    
    def compute_sh(self):
        pass
    
    def compute_sw(self):
        pass
    
    # J_TYPE
    def compute_jal(self):
        self.set_res(self.op_1 + self.op_2)
    
    # I_TYPE_JUMP
    def compute_jalr(self):
        self.set_res(self.op_1 + self.op_2)
    
    # U_TYPE_LOAD
    def compute_lui(self):
        self.set_res(self.get_op_2())
    
    # U_TYPE_ADD
    def compute_auipc(self):
        self.set_res(utils.remove_overflow(
            self.get_op_1() + self.get_op_2()) # Uncertain if needed overflow handling?
        )
    
    def compute_res(self):
        # R-type
        if self.get_ctrl() == const.ADD:
            self.compute_add()

        elif self.get_ctrl() == const.SUB:
            self.compute_sub() 
        
        elif self.get_ctrl() == const.XOR:
            self.compute_xor()

        elif self.get_ctrl() == const.OR:
            self.compute_or()
        
        elif self.get_ctrl() == const.AND:
            self.compute_and()

        elif self.get_ctrl() == const.SLL:
            self.compute_sll()

        elif self.get_ctrl() == const.SRL:
            self.compute_srl()                       

        elif self.get_ctrl() == const.SRA:
            self.compute_sra()

        elif self.get_ctrl() == const.SLT: 
            self.compute_slt()

        elif self.get_ctrl() == const.SLTU: 
            self.compute_sltu()

        # I-type
        elif self.get_ctrl() == const.ADDI: 
            self.compute_addi()
        
        elif self.get_ctrl() == const.XORI: 
            self.compute_xori()
        
        elif self.get_ctrl() == const.ORI: 
            self.compute_ori()
        
        elif self.get_ctrl() == const.ANDI: 
            self.compute_andi()
        
        elif self.get_ctrl() == const.SLLI: 
            self.compute_slli()
        
        elif self.get_ctrl() == const.SRLI: 
            self.compute_srli()
        
        elif self.get_ctrl() == const.SRAI: 
            self.compute_srai()
        
        elif self.get_ctrl() == const.SLTI: 
            self.compute_slti()
        
        elif self.get_ctrl() == const.SLTIU: 
            self.compute_sltiu()
        
        # I-type load
        elif self.get_ctrl() == const.LB: 
            self.compute_lb()
        
        elif self.get_ctrl() == const.LH: 
            self.compute_lh()
        
        elif self.get_ctrl() == const.LW: 
            self.compute_lw()
        
        elif self.get_ctrl() == const.LBU: 
            self.compute_lbu()
        
        elif self.get_ctrl() == const.LHU: 
            self.compute_lhu()
        
        # S-type
        elif self.get_ctrl() == const.SB: 
            self.compute_sb()
        
        elif self.get_ctrl() == const.SH: 
            self.compute_sh()
        
        elif self.get_ctrl() == const.SW: 
            self.compute_sw()
        
        # J_TYPE
        elif self.get_ctrl() == const.JAL:
            self.compute_jal()
            
        # I_TYPE_JUMP
        elif self.get_ctrl() == const.JALR:
            self.compute_jalr()
            
        # U_TYPE_LOAD
        elif self.get_ctrl() == const.LUI:
            self.compute_lui()
            

        # U_TYPE_ADD
        elif self.get_ctrl() == const.AUIPC:
            self.compute_auipc()
        
        # Unsupported operations
        else:
            pass
    
    def __repr__(self):
        return "ctrl: %s, op_1: %s, op_2: %s, res: %s" % (self.get_ctrl(), self.get_op_1(), self.get_op_2(), self.get_res())
        