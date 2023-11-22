# Implementation of Program Counter Class and functions 

# Program Counter Class
class ProgramCounter:
    def __init__(self, addr = 0):
        self.addr = addr
    
    def set_addr(self, new_addr):
        self.addr = new_addr
    
    def get_addr(self):
        return self.addr

    def print_fields(self):
        print(f"PC:")
        print(f" addr : {self.get_addr()}")
        print()
