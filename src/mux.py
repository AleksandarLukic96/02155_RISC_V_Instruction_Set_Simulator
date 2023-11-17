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
