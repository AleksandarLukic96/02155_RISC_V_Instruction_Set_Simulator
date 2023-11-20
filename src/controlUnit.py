# Implementation of ControlUnit Class and functions

# NOTES:
# Input: Opode 6:0, func7 6:0, func3 2:0
# Output: 1bit: Do_Branch, Do_Jump. reg_write, Mux_Reg, Mux_ALU, mem_write, reg_ctrl,
#          ALU_cnt 4:0,  mem_cnt 3:0, branch, imm 11:5 for I-types

# OPCODES
R_TYPE      = 0b0110011 #  51
I_TYPE      = 0b0010011 #  19
I_TYPE_LOAD = 0b0000011 #  19
S_TYPE      = 0b0100011 #  35
B_TYPE      = 0b1100011 #  99
J_TYPE      = 0b1101111 # 111
I_TYPE_JUMP = 0b1100111 # 103
U_TYPE_LOAD = 0b0110111 #  55
U_TYPE_ADD  = 0b0010111 #  23
I_TYPE_ENV  = 0b1110011 # 115

# ALU CTRL
# R-type
ADD   = 'ADD'
SUB   = 'SUB'
XOR   = 'XOR'
OR    = 'OR'
AND   = 'AND'
SLL   = 'SLL'
SRL   = 'SRL'
SRA   = 'SRA'
SLT   = 'SLT'
SLTU  = 'SLTU'

# I-type
ADDI  = 'ADDI'
XORI  = 'XORI'
ORI   = 'ORI'
ANDI  = 'ANDI'
SLLI  = 'SLLI'
SRLI  = 'SRLI'
SRAI  = 'SRAI'
SLTI  = 'SLTI'
SLTIU = 'SLTIU'

# I-type load
LB = 'LB'
LH = 'LH'
LW = 'LW'
LBU = 'LBU'
LHU = 'LHU'

# BRANCH CTRL
BEQ  = 'BEQ' # 0b00000 # 0
BNE  = 'BNE' # 0b00001 # 1
BLT  = 'BLT' # 0b00100 # 4
BGE  = 'BGE' # 0b00101 # 5
BLTU = 'BLTU' # 0b00110 # 6
BGEU = 'BGEU' # 0b00111 # 7

# REG CTRL
REG_FROM_DMEM = 0
REG_FROM_ALU = 1
REG_FROM_ADDER = 2

# ALU OP 1 CTRL
ALU_OP_1_FROM_REG = 0
ALU_OP_1_FROM_PC = 1

# ALU OP 2 CTRL
ALU_OP_2_FROM_REG = 0
ALU_OP_2_FROM_IMM = 1

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

        # Immidiate interpretation of func7
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

    # Immidiate
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

    # alu_op_1_ctrl: when 0, PC and when 1 = DATA1
    # alu_op_2_ctrl: When 0 = DATA2 and when 1 = Imm

    # Execution functions
    def execute_r_type(self):
        if (self.get_func3() == 0) & (self.get_func7() == 0):
            alu_ctrl = ADD

        elif (self.get_opcode() == 0) & (self.get_func7() == 20):
            alu_ctrl = SUB

        elif self.get_func3() == 4:
            alu_ctrl = XOR

        elif self.get_func3() == 6:
            alu_ctrl = OR

        elif self.get_func3() == 7:
            alu_ctrl = AND

        elif self.get_func3() == 1:
            alu_ctrl = SLL

        elif (self.get_func3() == 5) & (self.get_func7() == 0):
            alu_ctrl = SRL

        elif (self.get_func3() == 5) & (self.get_func7() == 20):
            alu_ctrl = SRA

        elif self.get_func3() == 2:
            alu_ctrl = SLT

        elif self.get_func3() == 3:
            alu_ctrl = SLTU

        else:
            print("This R-Type instruction is not supported!")
        
        #{'do_branch': 0, 'do_jump': 0, 'reg_write': 0, 'mem_write': 1, 
        # 'alu_op_1_ctrl': 1, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'ALU', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': alu_ctrl, 'mem_read': 0}
        
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = alu_ctrl) # <--- insert correct signals from the above line!

    def execute_i_type(self):
        if self.get_func3() == 0:
            alu_ctrl = ADDI

        elif self.get_func3() == 4:
            alu_ctrl = XORI

        elif  self.get_func3() == 6:
            alu_ctrl = ORI

        elif self.get_func3() == 7:
            alu_ctrl = ANDI

        elif (self.get_func3() == 1) & (self.get_imm() == 0):
            alu_ctrl = SLLI

        elif (self.get_func3() == 5) & (self.get_imm() == 0):
            alu_ctrl = SRLI

        elif (self.get_func3() == 5) & (self.get_imm() == 20):
            alu_ctrl = SRAI

        elif self.get_func3() == 2:
            alu_ctrl = SLTI

        elif self.get_func3() == 3:
            alu_ctrl = SLTIU

        else:
            print("This I-Type instruction is not supported!")
        
        #{'do_branch': 0, 'do_jump': 0, 'reg_write': 0, 'mem_write': 1, 
        # 'alu_op_1_ctrl': 1, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'ALU', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': alu_ctrl, 'mem_read': 0}
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = alu_ctrl)

    def execute_i_type_load(self):
        if self.get_func3() == 0:
            alu_ctrl = LB

        elif self.get_func3() == 1:
            alu_ctrl = LH

        elif self.get_func3() == 2:
            alu_ctrl = LW

        elif self.get_func3() == 4:
            alu_ctrl = LBU

        elif self.get_func3() == 5:
            alu_ctrl = LHU
        
        else:
            print("This I-Type Load instruction is not supported!")
        
        #{'do_branch': 0, 'do_jump': 0, 'reg_write': 0, 'mem_write': 0, 
        # 'alu_op_1_ctrl': 1, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'MEM', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': alu_ctrl, 'mem_read': 1}
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_DMEM, 
            mem_read = 1, 
            mem_write = 0, 
            alu_op_1_ctrl = ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = alu_ctrl)

    def execute_s_type(self):
        #SB
        if self.get_func3() == 0:
            s = 0 # What should happen here?
        #SH
        elif self.get_func3() == 1:
            s = 1 # What should happen here?
        #SW
        elif  self.get_func3() == 2:
            s = 2 # What should happen here?

        else:
            print("This S-Type instruction is not supported!")

        #{'do_branch': 0, 'do_jump': 0, 'reg_write': 0, 'mem_write': 1, 
        # 'alu_op_1_ctrl': 1, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'MEM', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 0, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_DMEM, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = ADD)

    def execute_b_type(self):
        if self.get_func3() == 0:
            branch_ctrl = BEQ
        
        elif self.get_func3() == 1:
            branch_ctrl = BNE
        
        elif self.get_func3()== 4:
            branch_ctrl = BLT
        
        elif self.get_func3() == 5:
            branch_ctrl = BGE
        
        elif self.get_func3() == 6:
            branch_ctrl = BLTU
        
        elif self.get_func3() == 7:
            branch_ctrl = BGEU
        
        else:
            print("This B-Type instruction is not supported!")
        
        #{'do_branch': 1, 'do_jump': 0, 'reg_write': 0, 'mem_write': 0, 
        # 'alu_op_1_ctrl': 0, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'MEM', 
        # 'branch_ctrl': branch, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = branch_ctrl, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_DMEM, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = ADD)

    def excute_j_type(self):
        #{'do_branch': 1, 'do_jump': 0, 'reg_write': 0, 'mem_write': 1, 
        # 'alu_op_1_ctrl': 0, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'PC4', 
        # 'branch_ctrl': 0b111, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = BGEU, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ADDER, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = ADD)

    def excute_i_type_jump(self):
        #{'do_branch': 1, 'do_jump': 0, 'reg_write': 0, 'mem_write': 1, 
        # 'alu_op_1_ctrl': 1, 'alu_op_2_ctrl': 0, 'reg_ctrl': 'PC4', 
        # 'branch_ctrl': 0b111, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = BGEU, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ADDER, 
            mem_read = 0, 
            mem_write = 1, 
            alu_op_1_ctrl = ALU_OP_1_FROM_REG, 
            alu_op_2_ctrl = ALU_OP_2_FROM_REG, 
            alu_ctrl = ADD)

    def excute_u_type_load(self):
        #{'do_branch': 1, 'do_jump': 0, 'reg_write': 0, 'mem_write': 0, 
        # 'alu_op_1_ctrl': 0, 'alu_op_2_ctrl': 1, 'reg_ctrl': 'IMM', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = ALU_OP_2_FROM_IMM, 
            alu_ctrl = ADD)

    def excute_u_type_add(self):        
        #{'do_branch': 1, 'do_jump': 0, 'reg_write': 0, 'mem_write': 0, 
        # 'alu_op_1_ctrl': 0, 'alu_op_2_ctrl': 1, 'reg_ctrl': 'ALU', 
        # 'branch_ctrl': 0b000, 'alu_ctrl': 'ADD', 'mem_read': 0}
        self.set_all_signals(
            do_branch = 1, 
            do_jump = 0, 
            branch_ctrl = BEQ, 
            reg_write = 0, 
            reg_ctrl = REG_FROM_ALU, 
            mem_read = 0, 
            mem_write = 0, 
            alu_op_1_ctrl = ALU_OP_1_FROM_PC, 
            alu_op_2_ctrl = ALU_OP_2_FROM_IMM, 
            alu_ctrl = ADD)

    def excute_i_type_env(self):
        if self.get_imm() == 0:
            # CALL
            self.set_all_signals() 
        
        elif self.get_imm() == 1:
            # BREAK
            self.set_all_signals()
        
        else:
            print("This I-Type Environment instruction is not supported!")
    
    def excute(self):
        # Interpret immidiate
        self.set_imm(self.get_func7() >> 5 )
        
        # Interpret opcode and update output signals accordingly
        if self.get_opcode() == R_TYPE:
            self.execute_r_type()
            
        elif self.get_opcode() == I_TYPE:
            self.execute_i_type()
        
        elif self.get_opcode() == I_TYPE_LOAD:
            self.execute_i_type_load()

        elif self.get_opcode() == S_TYPE:
            self.execute_s_type()
        
        elif self.get_opcode() == B_TYPE:
            self.execute_b_type()
        
        elif self.get_opcode() == J_TYPE:
            self.excute_j_type()
        
        elif self.get_opcode() == I_TYPE_JUMP: # and self.get_func3() == 0: <--- Is this neccessary?
            self.excute_i_type_jump()
        
        elif self.get_opcode() == U_TYPE_LOAD:
            self.excute_u_type_load()
        
        elif self.get_opcode() == U_TYPE_ADD:
            self.excute_u_type_add()
        
        elif self.get_opcode() == I_TYPE_ENV:
            self.excute_i_type_env()
        
        else:
            print("Opcode not supported")
            # TODO: Implement NOP - In case of invalid instruction, simply skip instruction by disabling any write/read signals!

    def print_fields(self):
        print(f"do_branch : {self.get_do_branch()}")
        print(f"do_jump: {self.get_do_jump()}")
        print(f"branch_ctrl: {self.get_branch_ctrl()}")
        print(f"reg_write: {self.get_reg_write()}")
        print(f"reg_ctrl: {self.get_reg_ctrl()}")
        print(f"mem_read: {self.get_mem_read()}")
        print(f"mem_write: {self.get_mem_write()}")
        print(f"alu_op_1_ctrl: {self.get_alu_op_1_ctrl()}")
        print(f"alu_op_2_ctrl: {self.get_alu_op_2_ctrl()}")
        print(f"alu_ctrl: {self.get_alu_ctrl()}")
        print()
        
# If file is run as python file, test class functions
if __name__ == "__main__":
    cu = ControlUnit()
    cu.print_fields()
    
    cu.set_opcode(19)
    cu.set_func3(0)
    cu.set_func7(3)
    cu.excute()
    cu.print_fields()
    
        
    