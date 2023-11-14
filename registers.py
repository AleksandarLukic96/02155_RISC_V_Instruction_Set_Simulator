# Implementation of Registers Class and functions 

# Instruction Memory Class
class Registers:
    def __init__(self):
        # Initialise registers
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0

        # Initialise 32 registers to 0
        self.regs = [0] * 32 

    # Format content of register to string as Binary, Hex or Integer
    def reg_str_bin(self, index):
        return "{0:032b}".format(self.regs[index])
    
    def reg_str_hex(self, index):
        return "{0:08x}".format(self.regs[index])

    def reg_str_int(self, index):
        return "{0:10}".format(self.regs[index])

    # Print content of all registers as Binary, Hex or Integer
    def print_regs_bin(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_str_bin(i)}")
    
    def print_regs_hex(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_str_hex(i)}")
    
    def print_regs_int(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_str_int(i)}")        
         

    
regs = Registers()
regs.print_regs_bin()
regs.print_regs_hex()
regs.print_regs_int()
