# Implementation of Registers Class and functions 
from ctypes import c_int32

# Function to handle 32-bit overflow
def int32(val):
    return c_int32(val).value

# Instruction Memory Class
class DataMemory:
    def __init__(self, mem_size = 1024):
        # Initialise size of memory
        self.mem_size = mem_size
        
        # Initialise empty memory
        self.mem_addrs = [0] * (self.mem_size // 4)
        
        # Initialise I/O
        self.addr = 0
        self.data_in = 0
        self.data_out = 0

        # Write Enabled signal
        self.write_enabled = 0
        
        # Read Enabled signal        
        self.read_enabled = 0

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
    
    def write_to_addr(self):
        if self.get_write_enabled() == 1:
            # Write data_in to address in memory
            self.mem_addrs[self.addr] = int32(self.data_in)    
    
    def read_from_addr(self):
        if self.get_read_enabled() == 1:
            # Read data_out from address in memory
            self.data_out = int32(self.mem_addrs[self.addr])


# If file is run as python file, test class functions
if __name__ == "__main__":
    dm = DataMemory()
    print(f"Capacity: {dm.mem_size} kiB = {len(dm.mem_addrs)} x 32-bit words")