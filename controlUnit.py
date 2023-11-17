# Implementation of ControlUnit Class and functions

# NOTES:
# Input: Opode 6:0, func7 6:0, func3 2:0
# Output: 1bit: Do_Branch, Do_Jump. WrReg, Mux_Reg, Mux_ALU, WRmem, WBsel,
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
BEQ  = 0b00000 # 0
BNE  = 0b00001 # 1
BLT  = 0b00100 # 4
BGE  = 0b00101 # 5
BLTU = 0b00110 # 6
BGEU = 0b00111 # 7

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

    # Execution functions
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
        
        # MUXReg: when 0, PC and when 1 = DATA1
        # MUXmem: When 0 = DATA2 and when 1 = Imm
        #{'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 0}
        self.set_all_signals(alu_ctrl = alu_ctrl) # <--- insert correct signals from the above line!

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
        
        #{'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 0}
        self.set_all_signals(alu_ctrl = alu_ctrl) # <--- insert correct signals from the above line!

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
        
        #{'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 1}
        self.set_all_signals(alu_ctrl = alu_ctrl) # <--- insert correct signals from the above line!

    def execute_s_type(self):
        #{'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def execute_b_type(self):
        if self.get_func3() == 0:
            branch = BEQ
        
        elif self.get_func3() == 1:
            branch = BNE
        
        elif self.get_func3()== 4:
            branch = BLT
        
        elif self.get_func3() == 5:
            branch = BGE
        
        elif self.get_func3() == 6:
            branch = BLTU
        
        elif self.get_func3() == 7:
            branch = BGEU
        
        else:
            print("This B-Type instruction is not supported!")
        
        #{'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': branch, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def excute_j_type(self):
        #{'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 0, 'MUXmem': 0, 'WBsel': 'PC4', 'branch': 0b111, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def excute_i_type_jump(self):
        #{'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'PC4', 'branch': 0b111, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def excute_u_type_load(self):
        #{'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 1, 'WBsel': 'IMM', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def excute_excute_u_type_add(self):        
        #{'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 1, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
        self.set_all_signals() # <--- insert correct signals from the above line!

    def excute_i_type_env(self):
        if self.get_imm() == 0:
            # CALL
            self.set_all_signals() 
        
        elif self.get_imm() == 1:
            # BREAK
            self.set_all_signals()
        
        else:
            print("This I-Type Environment instruction is not supported!")
