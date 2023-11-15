# Implementation of ALU Class and functions

# Declare operation constants
ADD  = 0b00000; # 0
SLL  = 0b00001; # 1
XOR  = 0b00100; # 4
OR   = 0b00110; # 6
AND  = 0b00111; # 7
SRL  = 0b00101; # 5
SUB  = 0b01000; # 8
SRA  = 0b01101; # 13
SLT  = 0b00010; # 2
SLTU = 0b00011; # 3

# ALU Class
class ALU:
    def __init__(self):
        # Inputs
        self.ctrl = 0
        self.op_1 = 0
        self.op_2 = 0
        
        # Output
        self.res = 0
        