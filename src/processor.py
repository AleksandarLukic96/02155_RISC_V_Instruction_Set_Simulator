# Implementation of Processor via connection between components 
from adder import Adder
from alu import ALU
from and_ import AND
from branch import Branch
from controlUnit import ControlUnit
from dataMemory import DataMemory
from decoder import Decoder
from immediate import Immediate
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
        self.imm = Immediate()
        self.imem = InstructionMemomry(file_path = file_path)
        self.pc = ProgramCounter()
        self.regs = Registers()
        
        # Initialise Multiplexors, Adder and logic gates
        self.mux2_1 = Mux2()
        self.mux2_2 = Mux2(in_0 = 2, in_1 = 4)
        self.mux2_3 = Mux2()
        self.mux2_4 = Mux2()
        self.mux3 = Mux3()
        self.adder = Adder()
        self.and_1 = AND()
        self.or_1 = OR()
    
    def execute_step(self):
        check = False
        
        # Prepare MUX for Adder (currently hardwired to 4)
        self.mux2_2.set_in_0(2)
        self.mux2_2.set_in_1(4)
        self.mux2_2.set_select(1) # Needs implementation from decoder? / Currently hardwired
        self.mux2_2.compute_out()
        if check == True:  print("Check 0")
        
        # Calculate next address for ProgramCounter
        self.adder.set_op_1(self.mux2_2.get_out())
        self.adder.set_op_2(self.pc.get_addr())
        self.adder.compute_out()
        if check == True:  print("Check 1")
        
        # Fetch instruction at current PC in instruction memory
        self.imem.set_addr(self.pc.get_addr())
        self.imem.fetch_inst_at_addr()
        if check == True:  print("Check 2")
        
        # Decode instruction
        self.dec.set_inst(self.imem.get_inst())
        self.dec.compute_decoding()
        if check == True:  print("Check 3")
                
        # Interpret decoded instruction in the Control Unit
        self.cu.set_opcode(self.dec.get_opcode())
        self.cu.set_func3(self.dec.get_func3())
        self.cu.set_func7(self.dec.get_func7())
        self.cu.excute()
        if check == True:  print("Check 4")
        
        # Handle imidiate interpretation from instruction
        self.imm.set_opcode(self.dec.get_opcode())
        self.imm.set_func3(self.dec.get_func3())
        self.imm.set_func7(self.dec.get_func7())
        self.imm.set_rd(self.dec.get_rd())
        self.imm.set_reg_1(self.dec.get_reg_1())
        self.imm.set_reg_2(self.dec.get_reg_2())
        self.imm.compute_res()
        if check == True:  print("Check 5")
        
        # Prepare Registers for instruction execution
        self.regs.set_write_enabled(self.cu.get_reg_write())
        self.regs.set_rd(self.dec.get_rd())
        self.regs.set_reg_1(self.dec.get_reg_1())
        self.regs.set_reg_2(self.dec.get_reg_2())
        if check == True:  print("Check 6")
        
        # Prepare MUX for alu operand 1
        self.mux2_3.set_in_0(self.pc.get_addr())
        self.mux2_3.set_in_1(self.regs.get_reg_1())
        self.mux2_3.set_select(self.cu.get_alu_op_1_ctrl())
        self.mux2_3.compute_out()
        if check == True:  print("Check 7")
        
        # Prepare MUX for alu operand 2
        self.mux2_4.set_in_0(self.regs.get_reg_2())
        self.mux2_4.set_in_1(self.imm.get_res())
        self.mux2_4.set_select(self.cu.get_alu_op_2_ctrl())
        self.mux2_4.compute_out()
        if check == True:  print("Check 8")
        
        # Execute operation in the ALU
        self.alu.set_op_1(self.mux2_3.get_out())      
        self.alu.set_op_2(self.mux2_4.get_out())
        self.alu.set_ctrl(self.cu.get_alu_ctrl())
        self.alu.compute_res()
        if check == True:  print("Check 9")
        
        # Write to or read from DataMemory if enabled
        self.dmem.set_addr(self.alu.get_res())
        self.dmem.set_data_in(self.regs.get_reg_2())
        self.dmem.set_read_enabled(self.cu.get_mem_read())
        self.dmem.set_write_enabled(self.cu.get_mem_write())
        self.dmem.read_from_addr()
        self.dmem.write_to_addr()
        if check == True:  print("Check 10")
        
        # Prepare MUX for Registers
        self.mux3.set_in_0(self.dmem.get_data_out())
        self.mux3.set_in_1(self.alu.get_res())
        self.mux3.set_in_2(self.adder.get_out())
        self.mux3.set_select(self.cu.get_reg_ctrl())
        self.mux3.compute_out()
        if check == True:  print("Check 11")
        
        # If writing is enabled then write to register rd
        self.regs.set_data_in(self.mux3.get_out())
        self.regs.write_to_rd()
        if check == True:  print("Check 12")
        
        # Update branch and assert if jump should be done
        self.bra.set_op_1(self.regs.get_reg_1())
        self.bra.set_op_2(self.regs.get_reg_2())
        self.bra.set_branch_ctrl(self.cu.get_branch_ctrl())
        if check == True:  print("Check 13")
        
        self.and_1.set_in_0(self.bra.get_branch_taken())
        self.and_1.set_in_1(self.cu.get_do_branch())
        self.and_1.compute_out()
        if check == True:  print("Check 14")
        
        self.or_1.set_in_0(self.and_1.get_out())
        self.or_1.set_in_1(self.cu.get_do_jump())
        self.or_1.compute_out()
        if check == True:  print("Check 15")
        
        # Prepare MUX for ProgramCounter
        self.mux2_1.set_in_0(self.adder.get_out())
        self.mux2_1.set_in_1(self.alu.get_res())
        self.mux2_1.set_select(self.or_1.get_out())
        self.mux2_1.compute_out()
        if check == True: print("Check 16") 
        
        # End sequence by updating PC
        self.pc.set_addr(self.mux2_1.get_out())
        if check == True:  print("Check 17")
    
    def execute_program():
        # TODO: Implement loop which executes every instruction in InstructionMemory
        pass


# If file is run as python file, test class functions
if __name__ == "__main__":

    # Test path
    import os
    file_path = os.path.join(
        os.getcwd(), "tests", "task1", "addlarge.bin")
        #os.getcwd(), "tests", "task4", "t15.bin")

    proc = Processor(file_path = file_path)
    
    for i in range(len(proc.regs.regs)):
        proc.regs.regs[i] = i
    
    for i in range(proc.imem.number_of_insts):
        proc.execute_step()
        print(f"\nAfter step execution of inst at ({i*4}):")
        proc.pc.print_fields()
        # print(f"mux2_2 out: {proc.mux2_2.get_out()}")
        proc.adder.print_fields()
        # str_hex = "{0:08x}".format(proc.imem.get_inst() % (1<<32))
        # print(f"imem inst: {str_hex} {proc.imem.get_inst()}")
        # print(f"imm res: {proc.imm.get_res()}")
        # print(f"dec Opcode: {proc.dec.get_opcode()}, func3: {proc.dec.get_func3()}, func7: {proc.dec.get_func7()}, rd: {proc.dec.get_rd()}, reg_1: {proc.dec.get_reg_1()}, reg_2: {proc.dec.get_reg_2()}")
        proc.cu.print_fields()
        proc.alu.print_fields()
        # print(f"Mux3 : {proc.mux3.get_select()}, out: {proc.mux3.get_out()}")
        proc.regs.print_fields()
        