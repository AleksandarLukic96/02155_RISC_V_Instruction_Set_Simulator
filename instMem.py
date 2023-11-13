#  Implementation of instruction memory  

import os

# Get path to test file
dir = os.getcwd()
test_folder = "tests"

# Choose task
task_1 = "task1"
task_2 = "task2"
task_3 = "task3"
task_4 = "task4"

# Choose test file 
file_names = [
    "addlarge.bin"
    ,"addneg.bin"
    ,"addpos.bin"
    ,"bool.bin"
    ,"set.bin"
    ,"shift.bin"
    ,"shift2.bin"
    ]
file_name = file_names[0]

# Concat into full file path
file_path = os.path.join(dir, test_folder, task_1, file_name)


# Load bin file into pyton
f = open(file_path, mode = "rb")
 
# Reading file data with read() method
data = f.read()
 
# Knowing the Type and size of our data
print(type(data))
print(f"{len(data)} bytes")
print(f"{len(data)//4} x 32-bit instructions")

# Concatinate bytes into 32-bit instructions as int-array
insts = []
i = 0 
while i < len(data):
    insts.append(
        (data[i+3] << 24) | 
        (data[i+2] << 16) | 
        (data[i+1] << 8) | 
        data[i])
    i = i + 4

# Print out program in binary, hex and decimal
i = 0
for inst in insts:
    str_bin = "{0:032b}".format(inst)
    str_hex = "{0:08x}".format(inst)
    str_int = "{0:10}".format(inst)
    str_opcode = "{0:07b}".format(inst & 127)
    str_i = "{0:3}".format(i)
    print(f"{str_i} Bin: {str_bin} Hex: {str_hex} Int: {str_int} Opcode: {str_opcode}")
    i = i + 1

# Closing the opened file
f.close()