# Implementation of Processor via connection between components 
from alu import ALU
from branch import Branch
from controlUnit import ControlUnit
from dataMemory import DataMemory
from decoder import Decoder
from instructionMemory import InstructionMemomry
from mux import Mux2, Mux3, Adder
from programCounter import ProgramCounter
from registers import Registers

# Test path
import os
file_path = os.path.join(
    os.getcwd(), "tests", "task1", "addlarge.bin")

# Initialise processor components
alu = ALU()
bra = Branch()
cu = ControlUnit()
dmem = DataMemory()
dec = Decoder()
imem = InstructionMemomry(file_path = file_path)
pc = ProgramCounter()
regs = Registers()

# Initialise Multiplexors
mux2_1 = Mux2(in_0 = 2, in_1 = 4)
mux2_2 = Mux2()
mux2_3 = Mux2()
mux2_4 = Mux2()
mux3 = Mux3()
adder = Adder()

# Wires 
# PC ----> InstructionMemory
imem.set_addr(pc.get_addr())

# PC ----> Adder
adder.set_op_2(pc.get_addr())
#adder.set_op_1(4) # If hardwired value

# PC ----> Mux2_3
mux2_3.set_in_1(pc.get_addr())

# InstructionMemory ----> Decoder 
dec.set_inst(imem.fetch_inst_at_addr())

# Decoder ----> Registers
regs.set_reg_1(dec.get_reg_1())
regs.set_reg_2(dec.get_reg_2())
regs.set_rd(dec.get_rd())

# Registers ----> Mux2_3
mux2_3.set_in_0(regs.get_reg_1())

# Registers ----> Mux2_4
mux2_4.set_in_0(regs.get_reg_2())

# Registers ----> Branch
bra.set_op_1(regs.get_reg_1())
bra.set_op_2(regs.get_reg_2())

# Registers ----> DataMemory
dmem.set_data_in(regs.get_reg_2())

# Mux2_3 ----> ALU
alu.set_op_1(mux2_3.get_out())

# Mux2_4 ----> ALU
alu.set_op_2(mux2_4.get_out())

# ALU ----> DataMemory
dmem.set_data_in(alu.get_res())

# DataMemory ----> Mux3
mux3.set_in_0(dmem.get_data_out())

# ALU ----> Mux3
mux3.set_in_1(alu.get_res())

# Adder ----> Mux3
mux3.set_in_2(adder.get_out())

# Mux3 ----> Registers
regs.set_data_in(dec.get_rd())

