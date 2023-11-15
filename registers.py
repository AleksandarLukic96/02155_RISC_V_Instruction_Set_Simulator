# Implementation of Registers Class and functions 
from ctypes import c_int32

# Function to handle 32-bit overflow
def int32(val):
    return c_int32(val).value

# Instruction Memory Class
class Registers:
    def __init__(self):
        # Initialise registers
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0

        # Write Enabled signal
        self.write_enabled = 0
        
        # Initialise 32 registers to 0
        self.regs = [0] * 32 

    def write_enable(self):
        self.write_enabled = 1
    
    def write_disable(self):
        self.write_enabled = 0
    
    def write_to_reg(self, data_in = 0):
        if self.write_enabled == 1:
            # Hardwired x0 to zero
            if self.rd == 0:
                return
            
            # Write data_in to register
            self.regs[self.rd] = int32(data_in)
    
    def set_reg_1(self, reg_no):
        self.reg_1 = reg_no
    
    def set_reg_2(self, reg_no):
        self.reg_2 = reg_no
    
    def get_reg_1(self):
        return self.reg_1
    
    def get_reg_2(self):
        return self.reg_2
    
    def set_rd(self, reg_no):
        self.rd = reg_no
    
    def return_reg_1_content(self):
        return self.regs[self.reg_1]
        
    def return_reg_2_content(self):
        return self.regs[self.reg_2]
    
    # Format content of register to string as Binary, Hex or Integer
    def reg_to_str_bin(self, index):
        return "{0:032b}".format(self.regs[index] % (1<<32))
    
    def reg_to_str_hex(self, index):
        return "{0:08x}".format(self.regs[index] % (1<<32))

    def reg_to_str_int(self, index):
        return "{0:10}".format(self.regs[index])

    # Print content of all registers as Binary, Hex or Integer
    def print_regs_bin(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_to_str_bin(i)}")
    
    def print_regs_hex(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_to_str_hex(i)}")
    
    def print_regs_int(self):
        for i in range(len(self.regs)):
            reg_name = "{0:3}".format("x" + str(i))
            print(f"{reg_name} : {self.reg_to_str_int(i)}")        
         

# If file is run as python file, test class functions
if __name__ == "__main__":
    rs = Registers()

    # This is how the registers should be written to
    for i in range(len(rs.regs)):
        rs.write_enable()
        rs.set_rd(i)
        if i % 2 == 0:
            rs.write_to_reg(data_in = i*4+4)
        else:
            rs.write_to_reg(data_in = -(i*4+4)) # Demostrating negative values
        rs.write_disable()

    rs.print_regs_bin()
    rs.print_regs_hex()
    rs.print_regs_int()

    print("\nSetting and getting registers via function calls:")
    rs.set_reg_1(11)
    rs.set_reg_2(22)
    print(f"x{rs.get_reg_1()}: {rs.return_reg_1()}")
    print(f"x{rs.get_reg_2()}: {rs.return_reg_2()}")
    