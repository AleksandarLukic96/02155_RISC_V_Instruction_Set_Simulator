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
import signal_constants as const
import utils

class Processor:
    def __init__(self, file_path = "NO_FILE_PROVIDED!", mem_size = const.MiB):
        # Initialise processor components
        self.alu = ALU()
        self.bra = Branch()
        self.cu = ControlUnit()
        self.dmem = DataMemory(file_path = file_path, mem_size = mem_size)
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

    def do_print_processor_fields(self):
        print("[PC         ]", self.pc)
        print("[MUX2_2     ]", self.mux2_2)
        print("[Adder      ]", self.adder)
        print("[Imemory    ]", self.imem)
        print("[Decoder    ]", self.dec)
        print("[Immediate  ]", self.imm)
        print("[ControlUnit]", self.cu)
        print("[MUX2_3     ]", self.mux2_3)
        print("[MUX2_4     ]", self.mux2_4)
        print("[ALU        ]", self.alu)
        print("[MUX3       ]", self.mux3)
        print("[Branch     ]", self.bra)
        print("[AND        ]", self.and_1)
        print("[OR         ]", self.or_1)
        print("[Registers  ]", self.regs)
        print("[MUX2_1     ]", self.mux2_1)
        print("[Dmemory    ]", self.dmem)
        
    def execute_step(self, do_print = False):
        check = False
        do_print = do_print
        pc_before_execution = self.pc.get_addr()
        if check == True:  print(f"PC: {self.pc.get_addr()}")
        
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
        self.mux2_3.set_in_0(self.regs.return_reg_1_content())
        self.mux2_3.set_in_1(self.pc.get_addr())
        self.mux2_3.set_select(self.cu.get_alu_op_1_ctrl())
        self.mux2_3.compute_out()
        if check == True:  print("Check 7")
        
        # Prepare MUX for alu operand 2
        self.mux2_4.set_in_0(self.regs.return_reg_2_content())
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
        self.dmem.set_data_in(self.regs.return_reg_2_content())
        self.dmem.set_read_enabled(self.cu.get_mem_read())
        self.dmem.set_write_enabled(self.cu.get_mem_write())
        self.dmem.set_inst_signal(self.cu.get_alu_ctrl())
        self.dmem.set_offset(self.imm.get_res())
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
        self.bra.set_op_1(self.regs.return_reg_1_content())
        self.bra.set_op_2(self.regs.return_reg_2_content())
        self.bra.set_branch_ctrl(self.cu.get_branch_ctrl())
        self.bra.compute_branch_taken()
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
        
        if do_print == True:
            print()
            print(f"Executed instruction from PC: {pc_before_execution}")
            self.do_print_processor_fields()
    
    def execute_program(self, do_print = False):
        do_print = do_print
        
        if do_print == False:
            while (self.pc.get_addr() <= len(self.imem.mem_slot)):             
                self.execute_step(do_print = do_print)
                if self.dec.get_opcode() == const.I_TYPE_ENV:
                    break
        else:
            while (self.pc.get_addr() <= len(self.imem.mem_slot)):
                self.execute_step(do_print = do_print)

                # Break loop at environment call
                if self.dec.get_opcode() == const.I_TYPE_ENV:
                    break
        
    def print_register_content_int_hex_bin(self):
        for i in range(len(self.regs.regs)):
            reg_name = "{:>3}".format("x" + str(i))
            print("%s %s" % (reg_name, utils.to_str_int_hex_bin(self.regs.regs[i]))) 
        
    def print_register_content(self, repr = 'hex'):
        repr = repr
        i = 0
        while i < len(self.regs.regs):
            if repr not in ['int', 'hex', 'bin']:
                self.print_register_content_int_hex_bin()
                break
            line = ""
            for j in range(4):
                reg_name = "{:>3}".format("x" + str(i+j))
                if repr == 'int':
                    reg_value = utils.to_str_int(self.regs.regs[i+j])
                elif repr == 'hex':
                    reg_value = utils.to_str_hex(self.regs.regs[i+j])
                elif repr == 'bin':
                    reg_value = utils.to_str_bin(self.regs.regs[i+j])
                line += reg_name + " = " + reg_value + ", "
            i += 4
            line = line[:-2]
            print(line)
