# Implementation of Processor via connection between components 
from alu import ALU
from branch import Branch
from controlUnit import ControlUnit
from dataMemory import DataMemory
from decoder import Decoder
from instructionMemory import InstructionMemomry
from programCounter import ProgramCounter
from registers import Registers

# Initialise processor components
alu = ALU()
bra = Branch()
cu = ControlUnit()
dmem = DataMemory()
dec = Decoder()
imem = InstructionMemomry()
pc = ProgramCounter()
regs = Registers()

# Wires 
# PC ----> InstructionMemory
imem.set_addr(pc.get_addr())

# InstructionMemory ----> Decoder 
dec.set_inst(imem.fetch_inst_at_addr())

# Decoder ----> Registers
regs.set_reg_1(dec.get_reg_1())
regs.set_reg_2(dec.get_reg_2())
regs.set_rd(dec.get_rd())

# Registers ----> Branch
bra.set_op_1(regs.get_reg_1())
bra.set_op_2(regs.get_reg_2())

# Registers ----> DataMemory
dmem.set_data_in(regs.get_reg_2())

# ALU ----> DataMemory
dmem.set_data_in(alu.get_res())
