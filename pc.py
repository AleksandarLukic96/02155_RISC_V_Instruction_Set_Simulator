from instMem import InstructionMemomry as imem
import decoder as dec

# Initialise Program Counter to 0
pc = 0

# temp path for testing
temp_path = "./tests/task1/addlarge.bin"

# Initialise Instruciton Memory
im = imem(file_path = temp_path, pc = pc)

# Testing Jump logic using update_pc(). 
im.update_pc(20)

while True:
    pc_str = "{0:3}".format(im.pc)
    print(f"PC: {pc_str} Inst: {im.fetch_inst_at_pc()}")
    
    # Using update_pc(), increment PC with a word / 32-bits / 4 bytes
    im.update_pc(im.pc + 4)
    
    if((im.pc >> 2) >= im.number_of_insts):
        break

# Print when exiting loop
print("Done")