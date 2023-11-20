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

class Processor:
    def __init__(self, file_path = "NO_FILE_PROVIDED!"):
        # Initialise processor components
        self.alu = ALU()
        self.bra = Branch()
        self.cu = ControlUnit()
        self.dmem = DataMemory()
        self.dec = Decoder()
        self.imem = InstructionMemomry(file_path = file_path)
        self.pc = ProgramCounter()
        self.regs = Registers()
        
        # Initialise Multiplexors, Adder and logic gates
        self.mux2_1 = Mux2(in_0 = 2, in_1 = 4)
        self.mux2_2 = Mux2()
        self.mux2_3 = Mux2()
        self.mux2_4 = Mux2()
        self.mux3 = Mux3()
        self.adder = Adder()
        self.and_1 = AND()
        self.or_1 = OR()
    
    def execute_step(self):        
        # Prepare MUX for Adder (currently hardwired to 4)
        self.mux2_2.set_in_0(2)
        self.mux2_2.set_in_1(4)
        self.mux2_2.set_select(1) # Needs implementation from decoder? / Currently hardwired
        self.mux2_2.compute_out
        
        # Calculate next address for ProgramCounter
        self.adder.set_op_1(self.mux2_2.get_out())
        self.adder.set_op_2(self.pc.get_addr())
        self.adder.compute_out
                
        # Fetch instruction at current PC in instruction memory
        self.imem.set_addr(self.pc.get_addr())
        self.imem.fetch_inst_at_addr()
        
        # Decode instruction
        self.dec.set_inst(self.imem.get_inst())
        self.dec.compute_decoding()
        
        # Interpret decoded instruction in the Control Unit
        self.cu.set_opcode(self.dec.get_opcode())
        self.cu.set_func3(self.dec.get_func3())
        self.cu.set_func3(self.dec.get_func7())
        # >> stuff happening here <<
        # >> stuff happening here <<
        # Needs implementation!
        # >> stuff happening here <<
        # >> stuff happening here <<
        self.cu.excute()
        
        # Handle imidiate interpretation from instruction
        # >> stuff happening here <<
        # Need implementation!
        # >> stuff happening here <<
                
        # Prepare MUX for alu
        self.mux2_3.set_in_0(self.pc.get_addr())
        self.mux2_3.set_in_1(self.regs.get_reg_1())
        self.mux2_3.set_select() # <--- Needs implementation!
        self.mux2_3.compute_out()
        
        # Prepare MUX for alu
        self.mux2_4.set_in_0(self.regs.get_reg_2())
        self.mux2_4.set_in_1() # <--- Needs implementation!
        self.mux2_4.set_select() # <--- Needs implementation!
        self.mux2_4.compute_out()
        
        # Execute operation in the ALU
        self.alu.set_op_1(self.mux2_3.get_out())      
        self.alu.set_op_2(self.mux2_4.get_out())
        self.alu.set_ctrl() # <--- Needs implementation!
        self.alu.compute_res()
        
        # Write to or read from DataMemory if enabled
        self.dmem.set_addr(self.alu.get_res())
        self.dmem.set_data_in(self.regs.get_reg_2())
        self.dmem.set_read_enabled() # <--- Needs implementation!
        self.dmem.set_write_enabled() # <--- Needs implementation!        
        self.dmem.read_from_addr()
        self.dmem.write_to_addr()
        
        # Prepare MUX for Registers
        self.mux3.set_in_0(self.dmem.get_data_out())
        self.mux3.set_in_1(self.alu.get_res())
        self.mux3.set_in_2(self.adder.get_out())
        self.mux3.set_select() # <--- Needs implementation!
        self.mux3.compute_out()
        
        # If writing is enabled then write to register rd
        self.regs.write_to_rd(self.mux3.get_out())
        
        # Update branch and assert if jump should be done
        self.bra.set_op_1(self.regs.get_reg_1())
        self.bra.set_op_2(self.regs.get_reg_2())
        self.bra.set_branch_ctrl() # <--- Needs implementation!
        
        self.and_1.set_in_0(self.bra.get_branch_taken())
        self.and_1.set_in_1() # <--- Needs implementation!
        self.and_1.compute_out()
        
        self.or_1.set_in_0(self.and_1.get_out())
        self.or_1.set_in_1() # <--- Needs implementation!
        self.or_1.compute_out()
        
        # Prepare MUX for ProgramCounter
        self.mux2_1.set_in_0(self.adder.get_out())
        self.mux2_1.set_in_1(self.alu.get_res())
        self.mux2_1.set_select(self.or_1.get_out())
        
        # End sequence by updating PC
        self.pc.set_addr(self.mux2_1.get_out())
        pass
    
    def execute_program():
        # TODO: Implement loop which executes every instruction in InstructionMemory
        pass


# If file is run as python file, test class functions
if __name__ == "__main__":

    # Test path
    import os
    file_path = os.path.join(
        os.getcwd(), "tests", "task1", "addlarge.bin")

    proc = Processor(file_path = file_path)
    proc.execute_step()
