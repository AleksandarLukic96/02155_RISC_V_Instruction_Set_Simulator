# Implementation of OR Class and functions

# OR Class
class OR:
    def __init__(self):
        self.in_0 = 0
        self.in_1 = 0
        self.out = 0
    
    def set_in_0(self, in_0):
        self.in_0 = 0 if in_0 == 0 else 1
    
    def get_in_0(self):
        return self.in_0

    def set_in_1(self, in_1):
        self.in_1 = 0 if in_1 == 0 else 1
    
    def get_in_1(self):
        return self.in_1

    def set_out(self, out):
        self.out = 0 if out == 0 else 1
    
    def get_out(self):
        return self.out
    
    def compute_out(self):
        self.set_out(
            self.get_in_0() | self.get_in_1()
        )

    def __repr__(self):
        return "in_0: %s, in_1: %s, out: %s" % (self.get_in_0(), self.get_in_1(), self.get_out())
    
    def print_fields(self):
        print(f"OR:")
        print(f" in_0 : {self.get_in_0()}")
        print(f" in_1 : {self.get_in_1()}")
        print(f" out  : {self.get_out()}")
        print()