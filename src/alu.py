# Implementation of ALU Class and functions
import signal_constants as const

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
        self.set_res(self.op_1 + self.op_2)

    def compute_sub(self):
        self.set_res(self.op_1 - self.op_2)
    
    def compute_xor(self):
        self.set_res(self.op_1 ^ self.op_2)
    
    def compute_or(self):
        self.set_res(self.op_1 | self.op_2)
    
    def compute_and(self):
        self.set_res(self.op_1 & self.op_2)
    
    def compute_sll(self):
        self.set_res(self.op_1 << self.op_2)
    
    def compute_srl(self):
        self.set_res(self.op_1 >> self.op_2)
    
    def compute_sra(self):
        self.set_res((self.op_1 >> self.op_2) if (self.op_1 >= 0) else ((self.op_1 + (1 << self.op_2) - 1) >> self.op_2))
    
    def compute_slt(self):
        self.set_res(0 | (self.op_1 < self.op_2)) 
    
    def compute_sltu(self):
        self.set_res(0 | (to_uint32(self.op_1) < to_uint32(self.op_2)))
    
    # I-type operations
    def compute_addi(self):
        pass
    
    def compute_xori(self):
        pass
    
    def compute_ori(self):
        pass
    
    def compute_andi(self):
        pass
    
    def compute_slli(self):
        pass
    
    def compute_srli(self):
        pass
    
    def compute_srai(self):
        pass
    
    def compute_slti(self):
        pass
    
    def compute_sltiu(self):
        pass
    
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
        pass
    
    # I_TYPE_JUMP
    def compute_jalr(self):
        pass
    
    # U_TYPE_LOAD
    def compute_lui(self):
        self.set_res(self.get_op_2() << 12)
    
    # U_TYPE_ADD
    def compute_auipc(self):
        pass    
    
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