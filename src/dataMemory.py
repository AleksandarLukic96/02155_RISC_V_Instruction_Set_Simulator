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
    def __init__(self, mem_size = MiB, file_path = "NO_FILE_GIVEN", little_endian = True):
        # Initialise size of memory
        self.mem_size = mem_size
    
        # Load bin file into pyton
        f = open(file_path, mode = "rb")
        
        # Reading file data with read() method
        self.data = f.read()
        
        # If False, then read bytes in big endian order
        self.little_endian = little_endian
        
        # Concatinate bytes into 32-bit instructions as int-array
        self.mem_addrs = [0] * self.mem_size
        
        # Stored as Little endian [LSB ----> MSB]        
        i = 0   
        if self.little_endian:
            while i < (len(self.data)):
                self.mem_addrs[i + 0] = self.data[i + 0]
                self.mem_addrs[i + 1] = self.data[i + 1]
                self.mem_addrs[i + 2] = self.data[i + 2]
                self.mem_addrs[i + 3] = self.data[i + 3]
                i += 4
        else:
            while i < (len(self.data)):
                self.mem_addrs[i + 0] = self.data[i + 3]
                self.mem_addrs[i + 1] = self.data[i + 2]
                self.mem_addrs[i + 2] = self.data[i + 1]
                self.mem_addrs[i + 3] = self.data[i + 0]
                i += 4
        
        # Closing the opened file
        f.close()
        
        # Initialise I/O
        self.addr = 0
        self.data_in = 0
        self.data_out = 0

        # Load/Save instruction signal
        self.inst_signal = 0
        
        # Offset from address byte/halfword/word
        self.offset = 0
        
        # Write Enabled signal
        self.write_enabled = 0
        
        # Read Enabled signal        
        self.read_enabled = 0
            
    def set_addr(self, addr):
        self.addr = addr
    
    def update_addr(self, addr):
        if self.write_enable == 1:
            self.set_addr(addr)
        else:
            pass
    
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
    
    def validate_signed_offset(self):
        if self.offset >> 31 == 1:
            self.offset = ~(self.offset ^ 0xFFFFFFFF)
    
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
        # split 32-bit input data into 4 bytes in Little endian order
        data_0 = (self.data_in & 0x000000FF) >>  0
        data_1 = (self.data_in & 0x0000FF00) >>  8
        data_2 = (self.data_in & 0x00FF0000) >> 16
        data_3 = (self.data_in & 0xFF000000) >> 24
        
        # If negative twos complement offset, then adapt python with workaround
        self.validate_signed_offset()
        
        if self.get_write_enabled() == 1:
            # Write data_in to address in memory
            if self.inst_signal == const.SB:
                self.mem_addrs[self.addr + 1*self.offset + 0] = data_0
            
            elif self.inst_signal == const.SH:
                self.mem_addrs[self.addr + 2*self.offset + 0] = data_0
                self.mem_addrs[self.addr + 2*self.offset + 1] = data_1
            
            elif self.inst_signal == const.SW:
                self.mem_addrs[self.addr + 4*self.offset + 0] = data_0
                self.mem_addrs[self.addr + 4*self.offset + 1] = data_1
                self.mem_addrs[self.addr + 4*self.offset + 2] = data_2
                self.mem_addrs[self.addr + 4*self.offset + 3] = data_3
                
            else:
                pass
            
    def read_from_addr(self):
        # Check for negative offset
        self.validate_signed_offset()
        
        if self.get_read_enabled() == 1:
            # Read 4 bytes from memory in Little endian and parse into output data order 32-bit data

            if self.inst_signal == const.LB:
                data_0 = self.mem_addrs[self.addr + 1*self.offset + 0]
                self.data_out = utils.sign_extend(data_0, 8)
                
            elif self.inst_signal == const.LH:
                data_0 = self.mem_addrs[self.addr + 2*self.offset + 0]
                data_1 = self.mem_addrs[self.addr + 2*self.offset + 1]
                self.data_out = utils.sign_extend(
                      (data_0 << 0)
                    | (data_1 << 8)
                    , 16)
                
            elif self.inst_signal == const.LW:
                data_0 = self.mem_addrs[self.addr + 2*self.offset + 0]
                data_1 = self.mem_addrs[self.addr + 2*self.offset + 1]
                data_2 = self.mem_addrs[self.addr + 1*self.offset + 2]
                data_3 = self.mem_addrs[self.addr + 1*self.offset + 3]
                self.data_out = utils.sign_extend(
                      (data_0 <<  0)
                    | (data_1 <<  8)
                    | (data_2 << 16)
                    | (data_3 << 24)
                    , 32)
                
            elif self.inst_signal == const.LBU:
                data_0 = self.mem_addrs[self.addr + 1*self.offset + 0]
                self.data_out = data_0
                
            elif self.inst_signal == const.LHU:
                data_0 = self.mem_addrs[self.addr + 2*self.offset + 0]
                data_1 = self.mem_addrs[self.addr + 2*self.offset + 1]
                self.data_out = (data_0 << 0) | (data_1 << 8)
            
            else:
                pass

    def __repr__(self):
        return "addr: %s, data_in: %s, data_out: %s, read_enabled: %s, write_enabled: %s" % (self.get_addr(), self.get_data_in(), self.get_data_out(), self.get_read_enabled(), self.get_write_enabled())
