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
ADD     = 'ADD'   # 0b00000 #  0
SUB     = 'SUB'   # 0b01000 #  8
XOR     = 'XOR'   # 0b00100 #  4
OR      = 'OR'    # 0b00110 #  6
AND     = 'AND'   # 0b00111 #  7
SLL     = 'SLL'   # 0b00001 #  1
SRL     = 'SRL'   # 0b00101 #  5
SRA     = 'SRA'   # 0b01101 # 13
SLT     = 'SLT'   # 0b00010 #  2
SLTU    = 'SLTU'  # 0b00011 #  3

# I-type
ADDI    = 'ADDI'  # 0b00000 # 0
XORI    = 'XORI'  # 0b00100 # 4
ORI     = 'ORI'   # 0b00110 # 6
ANDI    = 'ANDI'  # 0b00111 # 7
SLLI    = 'SLLI'  # 0b00001 # 1
SRLI    = 'SRLI'  # 0b00101 # 5
SRAI    = 'SRAI'  # 0b00101 # 5
SLTI    = 'SLTI'  # 0b00010 # 2
SLTIU   = 'SLTIU' # 0b00011 # 3

# I-type load
LB      = 'LB'    # 0b00000 # 0
LH      = 'LH'    # 0b00001 # 1
LW      = 'LW'    # 0b00010 # 2
LBU     = 'LBU'   # 0b00100 # 4
LHU     = 'LHU'   # 0b00101 # 5

# S-type
SB = 'SB'
SH = 'SH'
SW = 'SW'

# J-type
JAL     = 'JAL'   # 0b1101111 # 111

# I-type jump
JALR    = 'JALR'  # 0b1100111 # 103

# U-type load
LUI     = 'LUI'   # 0b0110111 # 55

# U-type add
AUIPC   = 'AUIPC' # 0b0010111 # 23

# BRANCH CTRL
BEQ     = 'BEQ'    # 0b00000 # 0
BNE     = 'BNE'    # 0b00001 # 1
BLT     = 'BLT'    # 0b00100 # 4
BGE     = 'BGE'    # 0b00101 # 5
BLTU    = 'BLTU'   # 0b00110 # 6
BGEU    = 'BGEU'   # 0b00111 # 7

# REG CTRL (Mux3)
REG_FROM_DMEM = 0
REG_FROM_ALU = 1
REG_FROM_ADDER = 2

# ALU OP 1 CTRL (Mux2_3)
ALU_OP_1_FROM_REG = 0
ALU_OP_1_FROM_PC = 1

# ALU OP 2 CTRL (Mux2_4)
ALU_OP_2_FROM_REG = 0
ALU_OP_2_FROM_IMM = 1
