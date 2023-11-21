# Implementation of Decoder Class and functions 

class Decoder:
    def __init__(self):
        # Read 32-bit instruction
        self.inst = 0
        
        # Split instruction into parts for decoding
        self.opcode = 0
        self.reg_1 = 0
        self.reg_2 = 0
        self.rd = 0
        self.func3 = 0
        self.func7 = 0
        
    def set_inst(self, inst):
        self.inst = inst

    def get_inst(self):
        return self.inst

    def set_opcode(self, opcode):
        self.opcode = opcode

    def get_opcode(self):
        return self.opcode

    def set_reg_1(self, reg_1):
        self.reg_1 = reg_1
    
    def get_reg_1(self):
        return self.reg_1

    def set_reg_2(self, reg_2):
        self.reg_2 = reg_2

    def get_reg_2(self):
        return self.reg_2

    def set_rd(self, rd):
        self.rd = rd
    
    def get_rd(self):
        return self.rd
    
    def set_func3(self, func3):
        self.func3 = func3
    
    def get_func3(self):
        return self.func3
    
    def set_func7(self, func7):
        self.func7 = func7
    
    def get_func7(self):
        return self.func7

    def compute_decoding(self):
        self.set_opcode(self.inst & 0b1111111)
        self.set_reg_1((self.inst >> 15) & 0b11111)
        self.set_reg_2((self.inst >> 20) & 0b11111)
        self.set_rd((self.inst >> 7) & 0b11111)
        self.set_func3((self.inst >> 12) & 0b111)
        self.set_func7((self.inst >> 25) & 0b1111111)

    def print_fields(self):
        print(f"get_inst(): {self.get_inst()}")
        print(f"get_opcode(): {self.get_opcode()}")
        print(f"get_reg_1(): {self.get_reg_1()}")
        print(f"get_reg_2(): {self.get_reg_2()}")
        print(f"get_rd(): {self.get_rd()}")
        print(f"get_func3(): {self.get_func3()}")
        print(f"get_func7(): {self.get_func7()}")
        print()
        
        
        
# If file is run as python file, test class functions
if __name__ == "__main__":
    dec = Decoder()
    dec.print_fields()
    
    test_inst = 0x80000537
    dec.set_inst(test_inst)
    dec.print_fields()
    
    dec.compute_decoding()
    dec.print_fields()
    
