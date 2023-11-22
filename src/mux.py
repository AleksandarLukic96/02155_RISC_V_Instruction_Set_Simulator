# Implementation of Mux Class and functions

# Multiplexor(Mux 2-to-1) Class
class Mux2:
    def __init__(self, in_0 = 0, in_1 = 1):
        self.in_0 = in_0
        self.in_1 = in_1
        self.select = 0
        self.out = 0

    def set_in_0(self, in_0):
        self.in_0 = in_0
    
    def get_in_0(self):
        return self.in_0
    
    def set_in_1(self, in_1):
        self.in_1 = in_1
    
    def get_in_1(self):
        return self.in_1
    
    def set_select(self, select):
        self.select = select
    
    def get_select(self):
        return self.select
    
    def compute_out(self):
        self.out = self.get_in_0() if self.get_select() == 0 else self.get_in_1()
    
    def get_out(self):
        return self.out
    
    def __repr__(self):
        return "in_0: %s, in_1: %s, select: %s, out: %s" % (self.get_in_0(), self.get_in_1(), self.get_select(), self.get_out())

    def print_fields(self):
        print(f"MUX2:")
        print(f" in_0   : {self.get_in_0()}")
        print(f" in_1   : {self.get_in_1()}")
        print(f" select : {self.get_select()}")
        print(f" out    : {self.get_out()}")
        print() 
    
# Multiplexor(Mux 3-to-1) Class 
class Mux3:
    def __init__(self, in_0 = 0, in_1 = 1, in_2 = 2):
        self.in_0 = in_0
        self.in_1 = in_1
        self.in_2 = in_2
        self.select = 0
        self.out = 0

    def set_in_0(self, in_0):
        self.in_0 = in_0
    
    def get_in_0(self):
        return self.in_0
    
    def set_in_1(self, in_1):
        self.in_1 = in_1
    
    def get_in_1(self):
        return self.in_1

    def set_in_2(self, in_2):
        self.in_2 = in_2
    
    def get_in_2(self):
        return self.in_2
    
    def set_select(self, select):
        self.select = select
    
    def get_select(self):
        return self.select
    
    def compute_out(self):
        if self.get_select() == 0:
            self.out = self.get_in_0()  
        elif self.get_select() == 1:
            self.out = self.get_in_1()
        elif self.get_select() == 2:
            self.out = self.get_in_2()
        else:
            pass
    
    def get_out(self):
        return self.out    
    
    def __repr__(self):
        return "in_0: %s, in_1: %s, in_2: %s, select: %s, out: %s" % (self.get_in_0(), self.get_in_1(), self.get_in_2(), self.get_select(), self.get_out())
        
    def print_fields(self):
        print(f"MUX3:")
        print(f" in_0   : {self.get_in_0()}")
        print(f" in_1   : {self.get_in_1()}")
        print(f" in_2   : {self.get_in_2()}")
        print(f" select : {self.get_select()}")
        print(f" out    : {self.get_out()}")
        print()
