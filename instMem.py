# Implementation of Instruction Memory Class and functions 
import os

# Instruction Memory Class
class InstructionMemomry:
    def __init__(self, file_path, pc = 0):
        
        # Load bin file into pyton
        f = open(file_path, mode = "rb")
        
        # Reading file data with read() method
        self.data = f.read()
        
        # Total number of instructions in program        
        self.number_of_insts = len(self.data) // 4
        
        # Set Program Counter as parsed, otherwise initialise to 0
        self.pc = pc
        
        # Concatinate bytes into 32-bit instructions as int-array
        self.insts = []
        
        i = 0
        while i < len(self.data):
            self.insts.append(
                (self.data[i + 3] << 24) | 
                (self.data[i + 2] << 16) | 
                (self.data[i + 1] <<  8) | 
                self.data[i])
            i += 4
        
        # Closing the opened file
        f.close()   
    
    # Update Program Counter to specific address    
    def update_pc(self, pc = 0):
        self.pc = pc
    
    # Return instruction at PC current address
    def fetch_inst_at_pc(self):
        return self.insts[self.pc // 4]
    
    # Printing to console functions
    def print_type(self):
        print(type(self.data))
    
    def print_bytes(self):
        print(f"{len(self.data)} bytes")
        
    def print_total_insts(self):
        print(f"{self.number_of_insts} x 32-bit instructions")
    
    def print_insts_bin(self):
        i = 0
        for inst in self.insts:
            str_bin = "{0:032b}".format(inst)
            str_i = "{0:3}".format(i)
            print(f"{str_i} Bin: {str_bin}")
            i += 1
    
    def print_insts_hex(self):
        i = 0
        for inst in self.insts:
            str_hex = "{0:08x}".format(inst)
            str_i = "{0:3}".format(i)
            print(f"{str_i} Hex: {str_hex}")
            i += 1
    
    def print_insts_int(self):
        i = 0
        for inst in self.insts:
            str_int = "{0:10}".format(inst)
            str_i = "{0:3}".format(i)
            print(f"{str_i} Int: {str_int}")
            i += 1
    
    def print_insts(self):
        # Print out program in binary, hex and decimal
        i = 0
        for inst in self.insts:
            str_bin = "{0:032b}".format(inst)
            str_hex = "{0:08x}".format(inst)
            str_int = "{0:10}".format(inst)
            str_opcode = "{0:07b}".format(inst & 127)
            str_i = "{0:3}".format(i)
            print(f"{str_i} Bin: {str_bin} Hex: {str_hex} Int: {str_int} Opcode: {str_opcode}")
            i += 1    


# If file run as python file, test class functions
if __name__ == "__main__":

    # Get path to test file
    dir = os.getcwd()
    test_folder = "tests"

    # Choose task
    task_1 = "task1"
    task_2 = "task2"
    task_3 = "task3"
    task_4 = "task4"

    # Choose test file 
    file_names = [
        "addlarge.bin"
        ,"addneg.bin"
        ,"addpos.bin"
        ,"bool.bin"
        ,"set.bin"
        ,"shift.bin"
        ,"shift2.bin"
        ]
    file_name = file_names[0]

    # Concat into full file path
    file_path = os.path.join(dir, test_folder, task_1, file_name)
    print(f"file_path:\n{file_path}")
    
    imem = InstructionMemomry(file_path = file_path)
    
    print("\nimem.print_type()")
    imem.print_type()
    print("\nimem.print_bytes()")
    imem.print_bytes()
    print("\nimem.print_total_insts()")
    imem.print_total_insts()
    print("\nimem.print_insts_bin()")
    imem.print_insts_bin()
    print("\nimem.print_insts_hex()")
    imem.print_insts_hex()
    print("\nimem.print_insts_int()")
    imem.print_insts_int()
    print("\nimem.print_insts():")
    imem.print_insts()
    