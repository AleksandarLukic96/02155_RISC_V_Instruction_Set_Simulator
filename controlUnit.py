 #DECODER
 #Input: Opode 6:0, func7 6:0, func3 2:0 
 #Output: 1bit: Do_Branch, Do_Jump. WrReg, Mux_Reg, Mux_ALU, WRmem, WBsel
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



def controlUnit(opcode, func3, func7):
    imm = func7 >> 5
    # R-Format
    if opcode == 0b0110011:
        if func3 == 0 and func7 == 0:
            ALUop = 'ADD'
        elif opcode == 0 and func7 == 20:
            ALUop = 'sub'
        elif func3 == 4:
            ALUop = 'XOR'
        elif func3 == 6:
            ALUop = 'OR'
        elif func3 == 7:
            ALUop = 'AND'
        elif func3 == 1:
            ALUop = 'SLL'
        elif func3 == 5 and func7 == 0:
            ALUop = 'SRL'
        elif func3 == 5 and func7 == 20:
            ALUop = 'SRA'
        elif func3 == 2:
            ALUop = 'SLT'
        elif func3 == 3:
            ALUop = 'SLTU'
        else:
            print("Opcode not supported")
        # MUXReg: when 0, PC and when 1 = DATA1
        # MUXmem: When 0 = DATA2 and when 1 = Imm
        return {'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 0}
#I-Format (imm)
    elif opcode == 0b0010011:
        if func3 == 0:
            ALUop = 'ADDI'
        elif func3 == 4:
            ALUop = 'XORI'
        elif  func3 == 6:
            ALUop = 'ORI'
        elif func3 == 7:
            ALUop = 'ANDI'
        elif func3 == 1 and imm == 0:
            ALUop = 'SLLI'
        elif func3 == 5 and imm == 0:
            ALUop = 'SRLI'
        elif func3 == 5 and imm == 20:
            ALUop = 'SRAI'
        elif func3 == 2:
            ALUop = 'SLTI'
        elif func3 == 3:
                ALUop = 'SLTIU'
        else:
            print("Opcode not supported")
        return {'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 0}
    #I-Format (Load)
    elif opcode == 0b0000011:
        if func3 == 0:
            ALUop = 'LB'
        elif func3 == 1:
            ALUop = ' LH'
        elif func3 == 2:
            ALUop = 'LW'
        elif func3 == 4:
            ALUop = ' LBU'
        elif func3 == 5:
            ALUop = 'LHU'
        else:
            print("Opcode not supported")
        return {'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': 0b000, 'ALUop': ALUop, 'mem_read': 1}
    #S-Format
    elif opcode == 0b0100011:
        return {'doBranch': 0, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
    #B-Format
    elif opcode == 0b1100011:
        if func3 == 0:
            branch = 0b001
        elif func3 == 1:
            branch = 0b010
        elif func3== 4:
            branch = 0b011
        elif func3 == 5:
            branch = 0b100
        elif func3 == 6:
            branch = 0b101
        elif func3 == 7:
            branch = 0b110
        else:
            print("Opcode not supported")
        return {'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 0, 'WBsel': 'MEM', 'branch': branch, 'ALUop': 'ADD', 'mem_read': 0}
    #JALR
    elif opcode == 0b1100111 and func3 == 0:
        return {'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 1, 'MUXmem': 0, 'WBsel': 'PC4', 'branch': 0b111, 'ALUop': 'ADD', 'mem_read': 0}
    #JAL
    elif opcode == 0b1101111:
        return {'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 1, 'MUXReg': 0, 'MUXmem': 0, 'WBsel': 'PC4', 'branch': 0b111, 'ALUop': 'ADD', 'mem_read': 0}
    #LUI
    elif opcode == 0b0110111:
        return {'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 1, 'WBsel': 'IMM', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
    #AUIPC
    elif opcode == 0b0010111:
        return {'doBranch': 1, 'doJump': 0, 'WrReg': 0, 'WRmem': 0, 'MUXReg': 0, 'MUXmem': 1, 'WBsel': 'ALU', 'branch': 0b000, 'ALUop': 'ADD', 'mem_read': 0}
    else:
        print("Opcode not supported")


