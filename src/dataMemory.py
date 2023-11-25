# Implementation of Registers Class and functions 
import signal_constants as const
import utils
import os

# Memory sizes in bytes
KB  = 1000
KiB = 1024
MB  = 1000000
MiB = 1048576
GB  = 1000000000
GiB = 1073741824

# Instruction Memory Class
class DataMemory:
    def __init__(self, mem_size = MiB, file_path = "NO_FILE_GIVEN", addr = 0, little_endian = True):
        # Initialise size of memory
        self.mem_size = mem_size
        
        # Initialise empty memory with indicies of bitdepth 4 bytes
        self.mem_addrs = [0] * (self.mem_size // 4)
        
        # Load bin file into pyton
        f = open(file_path, mode = "rb")
        
        # Reading file data with read() method
        self.data = f.read()
        
        # If False, then read bytes in big endian order
        self.little_endian = little_endian
        
        # Concatinate bytes into 32-bit instructions as int-array
        self.mem_slot = []
        
        i = 0   
        if self.little_endian:
            while i < (len(self.data)):
                self.mem_slot.append(
                    (self.data[i + 3] << 24) | 
                    (self.data[i + 2] << 16) | 
                    (self.data[i + 1] <<  8) | 
                    self.data[i])
                i += 4
        else:        
            while i < (len(self.data)):
                self.mem_slot.append(
                    (self.data[i] << 24) | 
                    (self.data[i + 1] << 16) | 
                    (self.data[i + 2] <<  8) | 
                    self.data[i + 3])
                i += 4

        i = 0   
        if self.little_endian:
            while i < (len(self.data)):
                self.mem_slot.append(self.data[i + 0])
                self.mem_slot.append(self.data[i + 1])
                self.mem_slot.append(self.data[i + 2])
                self.mem_slot.append(self.data[i + 3])
                i += 4
        else:
            while i < (len(self.data)):
                self.mem_slot.append(self.data[i + 3])
                self.mem_slot.append(self.data[i + 2])
                self.mem_slot.append(self.data[i + 1])
                self.mem_slot.append(self.data[i + 0])
                i += 4
        
        # Closing the opened file
        f.close()
        
        # Initialise I/O
        self.addr = 0
        self.data_in = 0
        self.data_out = 0

        # Load/Save instruction signal
        self.inst_signal = 0
        
        # Offset from address
        self.offset = 0
        
        # Write Enabled signal
        self.write_enabled = 0
        
        # Read Enabled signal        
        self.read_enabled = 0
            
    def set_addr(self, addr):
        self.addr = addr
    
    def get_addr(self):
        return self.addr
    
    def set_data_in(self, data_in):
        self.data_in = data_in
    
    def get_data_in(self):
        return self.data_in
    
    def set_data_out(self, data_out):
        self.data_out = data_out
    
    def get_data_out(self):
        return self.data_out
    
    def set_inst_signal(self, inst_signal):
        self.inst_signal = inst_signal
    
    def get_inst_signal(self):
        return self.inst_signal
    
    def set_offset(self, offset):
        self.offset = offset
    
    def get_offset(self):
        return self.offset
    
    def set_write_enabled(self, enable):
        self.write_enabled = enable
    
    def get_write_enabled(self):
        return self.write_enabled
    
    def write_enable(self):
        self.set_write_enabled(1)
    
    def write_disable(self):
        self.set_write_enabled(0)

    def set_read_enabled(self, enable):
        self.read_enabled = enable
    
    def get_read_enabled(self):
        return self.read_enabled
    
    def read_enable(self):
        self.set_read_enabled(1)
    
    def read_disable(self):
        self.set_read_enabled(0)
    
    def write_to_addr(self):
        if self.get_write_enabled() == 1:
            # Write data_in to address in memory
            if self.inst_signal == const.SB:
                    byte_value = utils.sign_extend((self.data_in & 0x000000FF), 8)
                    extend_value = byte_value >> 24
                    self.mem_addrs[self.addr] = byte_value
                    self.mem_addrs[self.addr] = byte_value
                    
            elif self.inst_signal == const.SH:
                self.mem_addrs[self.addr] = utils.sign_extend((self.data_in & 0x0000FFFF), 16)
            elif self.inst_signal == const.SW:
                self.mem_addrs[self.addr] = self.data_in
            else:
                pass
            
    def read_from_addr(self):
        if self.get_read_enabled() == 1:
            # Read data_out from address in memory
            if self.inst_signal == const.LB:
                self.data_out = utils.sign_extend(self.mem_addrs[self.addr][self.get_offset()], 8) 
            elif self.inst_signal == const.LH:
                self.data_out = utils.sign_extend((self.mem_addrs[self.addr] & 0x0000FFFF), 16)
            elif self.inst_signal == const.LW:
                self.data_out = self.mem_addrs[self.addr]
            elif self.inst_signal == const.LBU:
                self.data_out = (self.mem_addrs[self.addr] & 0xFF000000) >> 24
            elif self.inst_signal == const.LHU:
                self.data_out = (self.mem_addrs[self.addr] & 0xFFFF0000) >> 16
            else:
                pass

    def __repr__(self):
        return "addr: %s, data_in: %s, data_out: %s, read_enabled: %s, write_enabled: %s" % (self.get_addr(), self.get_data_in(), self.get_data_out(), self.get_read_enabled(), self.get_write_enabled())

# If file is run as python file, test class functions
if __name__ == "__main__":
    file_path = "C:/Users/Aleksandar/02155_RISC_V_Instruction_Set_Simulator/tests/bin_files_only/_t3_width.bin"
    dm = DataMemory(file_path = file_path)
    print(dm.mem_addrs[dm.addr][dm.get_offset()])
