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

    def __repr__(self):
        return "reg_1: %s, reg_2: %s, rd: %s, data_in: %s, write_enabled: %s" % (
            self.get_reg_1(), self.get_reg_2(), self.get_rd(), self.get_data_in(), self.get_write_enabled())
