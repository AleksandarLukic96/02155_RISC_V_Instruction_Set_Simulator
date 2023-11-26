# Implementation of Program Counter Class and functions 

# Program Counter Class
class ProgramCounter:
    def __init__(self, addr = 0):
        self.addr = addr
    
    def set_addr(self, new_addr):
        self.addr = new_addr
    
    def get_addr(self):
        return self.addr

    def __repr__(self):
        return "addr: %s" % (self.get_addr())
