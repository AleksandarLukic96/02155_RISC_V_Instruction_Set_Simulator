# Implementation of Instruction Memory Class and functions 
import os

# Instruction Memory Class
class InstructionMemomry:
    def __init__(self, file_path = "NO_FILE_GIVEN", addr = 0, little_endian = True):
        # Load bin file into pyton
        f = open(file_path, mode = "rb")
        

        # Reading file data with read() method
        self.data = f.read()
        
        # Set current address as parsed, otherwise initialise to 0
        self.addr = addr
        
        # Instruction is fetched into holder variable
        self.inst = 0
        
        # If False, then big endian
        self.little_endian = little_endian
        
        # Concatinate bytes into 32-bit instructions as int-array
        self.mem_slot = []
        
        i = 0   
        if self.little_endian:
            while i < (len(self.data)):
                self.mem_slot.append(self.data[i + 3])
                self.mem_slot.append(self.data[i + 2])
                self.mem_slot.append(self.data[i + 1])
                self.mem_slot.append(self.data[i + 0])
                i += 4
        else:
            while i < (len(self.data)):
                self.mem_slot.append(self.data[i + 0])
                self.mem_slot.append(self.data[i + 1])
                self.mem_slot.append(self.data[i + 2])
                self.mem_slot.append(self.data[i + 3])
                i += 4
        
        # Closing the opened file
        f.close()
        
    def set_addr(self, addr):
        self.addr = addr
    
    def get_addr(self):
        return self.addr
    
    def set_inst(self, inst):
        self.inst = inst
    
    def get_inst(self):
        return self.inst

    # Return 32-bit instruction from current address
    def fetch_inst_at_addr(self):
        i = 0   
        if self.little_endian:
            self.set_inst(
                  (self.mem_slot[self.addr + 0] << 24)
                | (self.mem_slot[self.addr + 1] << 16)
                | (self.mem_slot[self.addr + 2] <<  8) 
                | (self.mem_slot[self.addr + 3] <<  0)
            )
        else:
            self.set_inst(
                  (self.mem_slot[self.addr + 3] << 24)
                | (self.mem_slot[self.addr + 2] << 16)
                | (self.mem_slot[self.addr + 1] <<  8) 
                | (self.mem_slot[self.addr + 0] <<  0)
            )

    def __repr__(self):
        str_hex = "{0:08x}".format(self.get_inst() % (1<<32))
        return "addr: %s, inst: (int)%s, (hex)0x%s" % (self.get_addr(), self.get_inst(), str_hex)
