# Implementation of Registers Class and functions 

# Instruction Memory Class
class Registers:
    def __init__(self):
        # Initialise registers
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0

        # Initialise data input
        self.data_in = 0

        # Write Enabled signal
        self.write_enabled = 0

        # Initialise 32 registers to 0
        self.regs = [0] * 32 

    def set_reg_1(self, reg_1):
        if (reg_1 > 31) | (reg_1 < 0):
            pass
        else:
            self.reg_1 = reg_1

    def get_reg_1(self):
        return self.reg_1

    def set_reg_2(self, reg_2):
        if (reg_2 > 31) | (reg_2 < 0):
            pass
        else:
            self.reg_2 = reg_2

    def get_reg_2(self):
        return self.reg_2

    def set_rd(self, rd):
        if (rd > 31) | (rd < 0):
            pass
        else:
            self.rd = rd

    def get_rd(self):
        return self.rd

    def set_data_in(self, data_in):
        self.data_in = data_in

    def get_data_in(self):
        return self.data_in

    def set_write_enabled(self, enable):
        self.write_enabled = enable

    def get_write_enabled(self):
        return self.write_enabled

    def write_enable(self):
        self.set_write_enabled(1)

    def write_disable(self):
        self.set_write_enabled(0)

    def return_reg_1_content(self):
        return self.regs[self.get_reg_1()]

    def return_reg_2_content(self):
        return self.regs[self.get_reg_2()]

    def write_to_rd(self):
        if self.get_write_enabled() == 1:
            # Hardwired x0 to zero
            if self.get_rd() == 0:
                return

            # Write data_in to register
            self.regs[self.get_rd()] = self.get_data_in()

    def print_fields(self):
        print(f"Registers:")
        print(f"reg_1         : {self.get_reg_1()}")
        print(f"reg_2         : {self.get_reg_2()}")
        print(f"rd            : {self.get_rd()}")
        print(f"data_in       : {self.get_data_in()}")
        print(f"write_enabled : {self.get_write_enabled()}")
        print()

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
            rs.set_data_in(i*4+4)
            rs.write_to_rd()
        else:
            rs.set_data_in(-(i*4+4)) # Demostrating negative values
            rs.write_to_rd()
        rs.write_disable()

    rs.print_regs_bin()
    rs.print_regs_hex()
    rs.print_regs_int()

    print("\nSetting and getting registers via function calls:")
    rs.set_reg_1(11)
    rs.set_reg_2(22)
    print(f"x{rs.get_reg_1()}: {rs.return_reg_1_content()}")
    print(f"x{rs.get_reg_2()}: {rs.return_reg_2_content()}")
    