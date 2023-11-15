# Implementation of Processor via connection between components 
from alu import ALU
from controlUnit import ControlUnit
from dataMemory import DataMemory
from decoder import Decoder
from instructionMemory import InstructionMemomry
from programCounter import ProgramCounter
from registers import Registers

# Initialise processor components
alu = ALU()
cu = ControlUnit()
dmem = DataMemory()
dec = Decoder()
imem = InstructionMemomry()
pc = ProgramCounter()
regs = Registers()


