 #DECODER
 #Input: One 32 bit instruction 
 #Output: 3x4bit registers -> rs1, rs2 and rsd
#         32 bit instruction and 6 bit opcode
#         7bit func7 and 3bit func3
def decode(instruction): 
    opcode = instruction & 0b1111111
    rs1 = (instruction >> 15) & 0b11111
    rs2 =  (instruction >> 20) & 0b11111
    rsd =  (instruction >> 7) & 0b11111
    func7 = (instruction >> 25)
    func3 = (instruction >> 12) & 0b111

    return rs1, rs2, rsd, opcode, instruction, func7, func3


