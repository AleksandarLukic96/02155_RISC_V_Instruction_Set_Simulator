# Implementation of Program Counter Class and functions 
#from instructionMemory import InstructionMemomry

# Program Counter Class
class ProgramCounter:
    def __init__(self, addr = 0):
        self.addr = addr
    
    def set_addr(self, new_addr):
        self.addr = new_addr
    
    def get_addr(self):
        return self.addr


# If file is run as python file, test class functions
# if __name__ == "__main__":

#     pc = ProgramCounter()

#     # temp path for testing
#     temp_path = "./tests/task1/addlarge.bin"

#     # Initialise Instruciton Memory
#     im = InstructionMemomry(file_path = temp_path, addr = pc.get_addr())

#     while True:
#         pc_str = "{0:3}".format(pc.addr)
#         print(f"PC: {pc_str} Inst: {im.fetch_inst_at_addr()}")
        
#         # Testing Jump logic
#         if pc.get_addr() == 12:
#             new_addr = 20
#             print(f"Jump from {im.addr} to {new_addr}")
#             pc.set_addr(new_addr)
#             im.set_addr(pc.get_addr())
#         else:
#             # Increment PC and update address in inst memory
#             pc.set_addr(pc.get_addr() + 4)
#             im.set_addr(pc.get_addr())
            
#         if((pc.addr >> 2) >= im.number_of_insts):
#             break

#     # Print when exiting loop
#     print("Done")
