from instMem import InstructionMemomry as imem
import decoder as dec

# Initialise Program Counter to 0
pc = 0

# temp path for testing
temp_path = "./tests/task1/addlarge.bin"

# Initialise Instruciton Memory
im = imem(file_path = temp_path, pc = pc)

while True:
    pc_str = "{0:3}".format(im.pc)
    print(f"PC: {pc_str} Inst: {im.insts[im.pc//4]}")
    
    im.pc += 4
    
    if((im.pc >> 2) >= len(im.insts)):
        break

# Print when exiting loop
print("Done")

