# Implementation of ControlUnit Class and functions
import signal_constants as const

# NOTES:
# Input: Opode 6:0, func7 6:0, func3 2:0
# Output: 1bit: Do_Branch, Do_Jump. reg_write, Mux_Reg, Mux_ALU, mem_write, reg_ctrl,
#          ALU_cnt 4:0,  mem_cnt 3:0, branch, imm 11:5 for I-types

# Control Unit Class
class ControlUnit:
    def __init__(self):
        # Input for interpreting
        self.func3 = 0
        self.func7 = 0
        self.opcode = 0

        # Output Control signals
        self.do_branch = 0
        self.do_jump = 0
        self.branch_ctrl = 0
        self.reg_write = 0
        self.reg_ctrl = 0
        self.mem_read = 0
        self.mem_write = 0
        self.alu_op_1_ctrl = 0
        self.alu_op_2_ctrl = 0
        self.alu_ctrl = 0 

        # Immediate interpretation of func7
        self.imm = 0

    # Input Setters and Getters
    def set_func3(self, func3):
        self.func3 = func3

    def get_func3(self):
        return self.func3

    def set_func7(self, func7):
        self.func7 = func7

    def get_func7(self):
        return self.func7

    def set_opcode(self, opcode):
        self.opcode = opcode

    def get_opcode(self):
        return self.opcode

    # Output Setters and Getters
    def set_do_branch(self, do_branch):
        self.do_branch = do_branch 

    def get_do_branch(self):
        return self.do_branch

    def set_do_jump(self, do_jump):
        self.do_jump = do_jump

    def get_do_jump(self):
        return self.do_jump

    def set_branch_ctrl(self, branch_ctrl):
        self.branch_ctrl = branch_ctrl

    def get_branch_ctrl(self):
        return self.branch_ctrl

    def set_reg_write(self, reg_write):
        self.reg_write = reg_write

    def get_reg_write(self):
        return self.reg_write

    def set_reg_ctrl(self, reg_ctrl):
        self.reg_ctrl = reg_ctrl

    def get_reg_ctrl(self):
        return self.reg_ctrl

    def set_mem_read(self, mem_read):
        self.mem_read = mem_read

    def get_mem_read(self):
        return self.mem_read

    def set_mem_write(self, mem_write):
        self.mem_write = mem_write

    def get_mem_write(self):
        return self.mem_write

    def set_alu_op_1_ctrl(self, alu_op_1_ctrl):
        self.alu_op_1_ctrl = alu_op_1_ctrl 

    def get_alu_op_1_ctrl(self):
        return self.alu_op_1_ctrl

    def set_alu_op_2_ctrl(self, alu_op_2_ctrl):
        self.alu_op_2_ctrl = alu_op_2_ctrl

    def get_alu_op_2_ctrl(self):
        return self.alu_op_2_ctrl

    def set_alu_ctrl(self, alu_ctrl):
        self.alu_ctrl = alu_ctrl

    def get_alu_ctrl(self):
        return self.alu_ctrl

    # Immediate
    def set_imm(self, imm):
        self.imm = imm

    def get_imm(self):
        return self.imm

    # Set all singals
    def set_all_signals(self, do_branch, do_jump, branch_ctrl, reg_write, reg_ctrl, mem_read, mem_write, alu_op_1_ctrl, alu_op_2_ctrl, alu_ctrl):
        self.set_do_branch(do_branch)
        self.set_do_jump(do_jump)
        self.set_branch_ctrl(branch_ctrl)
        self.set_reg_write(reg_write)
        self.set_reg_ctrl(reg_ctrl)
        self.set_mem_read(mem_read)
        self.set_mem_write(mem_write)
        self.set_alu_op_1_ctrl(alu_op_1_ctrl)
        self.set_alu_op_2_ctrl(alu_op_2_ctrl)
        self.set_alu_ctrl(alu_ctrl)

    # Execution functions
    def execute_nop(self):
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 0, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_REG, 
            alu_ctrl = const.ADD)
    
    def execute_r_type(self):
        if (self.get_func3() == 0x0) & (self.get_func7() == 0x00):
            alu_ctrl = const.ADD

        elif (self.get_func3() == 0x0) & (self.get_func7() == 0x20):
            alu_ctrl = const.SUB

        elif self.get_func3() == 0x4:
            alu_ctrl = const.XOR

        elif self.get_func3() == 0x6:
            alu_ctrl = const.OR

        elif self.get_func3() == 0x7:
            alu_ctrl = const.AND

        elif self.get_func3() == 0x1:
            alu_ctrl = const.SLL

        elif (self.get_func3() == 0x5) & (self.get_func7() == 0x00):
            alu_ctrl = const.SRL

        elif (self.get_func3() == 0x5) & (self.get_func7() == 0x20):
            alu_ctrl = const.SRA

        elif self.get_func3() == 0x2:
            alu_ctrl = const.SLT

        elif self.get_func3() == 0x3:
            alu_ctrl = const.SLTU

        else:
            print("This R-Type instruction is not supported!")
        
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_REG, 
            alu_ctrl = alu_ctrl)

    def execute_i_type(self):
        if self.get_func3() == 0x0:
            alu_ctrl = const.ADDI

        elif self.get_func3() == 0x4:
            alu_ctrl = const.XORI

        elif  self.get_func3() == 0x6:
            alu_ctrl = const.ORI

        elif self.get_func3() == 0x7:
            alu_ctrl = const.ANDI

        elif (self.get_func3() == 0x1) & (self.get_imm() == 0x00):
            alu_ctrl = const.SLLI

        elif (self.get_func3() == 0x5) & (self.get_imm() == 0x00):
            alu_ctrl = const.SRLI

        elif (self.get_func3() == 0x5) & (self.get_imm() == 0x20):
            alu_ctrl = const.SRAI

        elif self.get_func3() == 0x2:
            alu_ctrl = const.SLTI

        elif self.get_func3() == 0x3:
            alu_ctrl = const.SLTIU

        else:
            print("This I-Type instruction is not supported!")

        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = alu_ctrl)

    def execute_i_type_load(self):
        if self.get_func3() == 0x0:
            alu_ctrl = const.LB

        elif self.get_func3() == 0x1:
            alu_ctrl = const.LH

        elif self.get_func3() == 0x2:
            alu_ctrl = const.LW

        elif self.get_func3() == 0x4:
            alu_ctrl = const.LBU

        elif self.get_func3() == 0x5:
            alu_ctrl = const.LHU
        
        else:
            print("This I-Type Load instruction is not supported!")
        
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_DMEM, 
            mem_read = 1, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = alu_ctrl)

    def execute_s_type(self):
        if self.get_func3() == 0x0:
            alu_ctrl = const.SB
        
        elif self.get_func3() == 0x1:
            alu_ctrl = const.SH
        
        elif  self.get_func3() == 0x2:
            alu_ctrl = const.SW

        else:
            print("This S-Type instruction is not supported!")

        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 0, 
            reg_ctrl = const.REG_FROM_DMEM, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = alu_ctrl)

    def execute_b_type(self):
        if self.get_func3() == 0x0:
            branch_ctrl = const.BEQ
        
        elif self.get_func3() == 0x1:
            branch_ctrl = const.BNE
        
        elif self.get_func3()== 0x4:
            branch_ctrl = const.BLT
        
        elif self.get_func3() == 0x5:
            branch_ctrl = const.BGE
        
        elif self.get_func3() == 0x6:
            branch_ctrl = const.BLTU
        
        elif self.get_func3() == 0x7:
            branch_ctrl = const.BGEU
        
        else:
            print("This B-Type instruction is not supported!")

        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = branch_ctrl, 
            reg_write = 0, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = const.ADDI)

    def execute_j_type(self):
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 1, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_ADDER, 
            mem_read = 0,
            mem_write = 0,
            alu_op_1_ctrl = const.ALU_OP_1_FROM_PC,
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM,
            alu_ctrl = const.JAL)

    def execute_i_type_jump(self):
        self.set_all_signals(
            do_branch = 0,
            do_jump = 1,
            branch_ctrl = const.BEQ,
            reg_write = 1,
            reg_ctrl = const.REG_FROM_ADDER,
            mem_read = 0,
            mem_write = 0,
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG,
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM,
            alu_ctrl = const.JALR)

    def execute_u_type_load(self):
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = const.LUI)

    def execute_u_type_add(self):        
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = const.BEQ, 
            reg_write = 1, 
            reg_ctrl = const.REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = const.ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = const.ALU_OP_2_FROM_IMM, 
            alu_ctrl = const.AUIPC)

    def execute_i_type_env(self):
        if self.get_imm() == 0x0:
            # ECALL <--- Needs to be implemented!
            self.execute_nop() 
        
        elif self.get_imm() == 0x1:
            # EBREAK <--- Needs to be implemented!
            self.execute_nop() 
        
        else:
            print("This I-Type Environment instruction is not supported!")
    
    def excute(self):
        # Interpret immediate
        self.set_imm(self.get_func7())
        
        # Interpret opcode and update output signals accordingly
        if self.get_opcode() == const.R_TYPE:
            self.execute_r_type()
            
        elif self.get_opcode() == const.I_TYPE:
            self.execute_i_type()
        
        elif self.get_opcode() == const.I_TYPE_LOAD:
            self.execute_i_type_load()

        elif self.get_opcode() == const.S_TYPE:
            self.execute_s_type()
        
        elif self.get_opcode() == const.B_TYPE:
            self.execute_b_type()
        
        elif self.get_opcode() == const.J_TYPE:
            self.execute_j_type()
        
        elif self.get_opcode() == const.I_TYPE_JUMP:
            self.execute_i_type_jump()
        
        elif self.get_opcode() == const.U_TYPE_LOAD:
            self.execute_u_type_load()
        
        elif self.get_opcode() == const.U_TYPE_ADD:
            self.execute_u_type_add()
        
        elif self.get_opcode() == const.I_TYPE_ENV:
            self.execute_i_type_env()
        
        else:
            print("Opcode not supported")
            self.execute_nop()

    def __repr__(self):
        return "do_branch: %s, do_jump: %s, branch_ctrl: %s, reg_write: %s, reg_ctrl: %s, mem_read: %s, mem_write: %s, alu_op_1_ctrl: %s, alu_op_2_ctrl: %s, alu_ctrl: %s" % (
            self.get_do_branch(), self.get_do_jump(), self.get_branch_ctrl(), self.get_reg_write(), self.get_reg_ctrl(), self.get_mem_read(), self.get_mem_write(), self.get_alu_op_1_ctrl(), self.get_alu_op_2_ctrl(), self.get_alu_ctrl())
    
    def print_fields(self):
        print(f"ControlUnit:")
        print(f" do_branch    : {self.get_do_branch()}")
        print(f" do_jump      : {self.get_do_jump()}")
        print(f" branch_ctrl  : {self.get_branch_ctrl()}")
        print(f" reg_write    : {self.get_reg_write()}")
        print(f" reg_ctrl     : {self.get_reg_ctrl()}")
        print(f" mem_read     : {self.get_mem_read()}")
        print(f" mem_write    : {self.get_mem_write()}")
        print(f" alu_op_1_ctrl: {self.get_alu_op_1_ctrl()}")
        print(f" alu_op_2_ctrl: {self.get_alu_op_2_ctrl()}")
        print(f" alu_ctrl     : {self.get_alu_ctrl()}")
        print()

if __name__ == "__main__":
    cu = ControlUnit()
    cu.set_opcode(51)
    cu.set_func3(0)
    cu.set_func7(0x20)

    
    cu.excute()
    
    print(cu)
    