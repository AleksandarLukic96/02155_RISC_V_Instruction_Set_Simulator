# Implementation of Processor via connection between components 
from adder import Adder
from alu import ALU
from and_ import AND
from branch import Branch
from controlUnit import ControlUnit
from dataMemory import DataMemory
from decoder import Decoder
from instructionMemory import InstructionMemomry
from mux import Mux2, Mux3
from or_ import OR
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

# Initialise Multiplexors, Adder and logic gates
mux2_1 = Mux2(in_0 = 2, in_1 = 4)
mux2_2 = Mux2()
mux2_3 = Mux2()
mux2_4 = Mux2()
mux3 = Mux3()
adder = Adder()
and_1 = AND()
or_1 = OR()

# Wires listed by component inputs

# Mux2_1
mux2_1.set_in_0(adder.get_out())
mux2_1.set_in_1(alu.get_res())
mux2_1.set_select(or_1.get_out())

# Mux2_2
mux2_2.set_in_0(2)
mux2_2.set_in_1(4)
mux2_2.set_select(1) # Needs implementation from decoder? / Currently hardwired

# PC
pc.set_addr(mux2_1.get_out())

# Adder
adder.set_op_1(mux2_2.get_out)
adder.set_op_2(pc.get_addr())

# InstructionMemory
imem.set_addr(pc.get_addr())

# Decoder 
dec.set_inst(imem.fetch_inst_at_addr())

# Immidiate
 # Needs implementation 

# ControlUnit
 # Needs implementation 

# Registers
regs.set_reg_1(dec.get_reg_1())
regs.set_reg_2(dec.get_reg_2())
regs.set_rd(dec.get_rd())
regs.set_data_in(dec.get_rd())
regs.set_write_enabled(cu.get_reg_write())

# Mux2_3
mux2_3.set_in_0(regs.get_reg_1())
mux2_3.set_in_1(pc.get_addr())
mux2_3.set_select(cu.get_alu_op_1_ctrl())

# Branch
bra.set_op_1(regs.get_reg_1())
bra.set_op_2(regs.get_reg_2())
bra.set_branch_ctrl(cu.get_branch_ctrl())

# Mux2_4
mux2_4.set_in_0(regs.get_reg_2())
#mux2_4.set_in_1(imm.get_imm_out()) # Needs implementation 
mux2_4.set_select(cu.get_alu_op_1_ctr2())

# ALU
alu.set_op_1(mux2_3.get_out())
alu.set_op_2(mux2_4.get_out())
alu.set_ctrl(cu.get_alu_ctrl())

# AND
and_1.set_in_0(bra.get_branch_taken())
and_1.set_in_1(cu.get_do_branch())

# OR
or_1.set_in_0(and_1.get_out())
or_1.set_in_1(cu.get_do_jump())

# DataMemory
dmem.set_addr(alu.get_res())
dmem.set_data_in(regs.get_reg_2())
dmem.set_read_enabled(cu.get_mem_read())
dmem.set_write_enabled(cu.get_mem_write())

# Mux3
mux3.set_in_0(dmem.get_data_out())
mux3.set_in_1(alu.get_res())
mux3.set_in_2(adder.get_out())
mux3.set_select(cu.get_reg_ctrl())
