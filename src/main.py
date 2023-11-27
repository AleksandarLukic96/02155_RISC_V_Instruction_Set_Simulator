import os
from processor import Processor
import signal_constants as const

def print_intro():
    width = 50
    str_1 = '{: ^{width}}'.format("RISC-V Single Cycle Instruction Set Simulation", width = width)
    str_2 = '{: ^{width}}'.format("This program loads a given binary file,", width = width)
    str_3 = '{: ^{width}}'.format("and interprets it as a RISC-V program.", width = width)
    str_0 = "#" * width
    print()
    print(f"##{str_0}##")
    print(f"##{str_1}##")
    print(f"##{str_2}##")
    print(f"##{str_3}##")
    print(f"##{str_0}##")
    print()

def print_help_menu():
    print("Help Menu: ")
    print(" 'h' : Print out actions to terminal.")
    print(" 'f' : Provide file path to binary file.")
    print(" 's' : Execute current instruction at PC.")
    print(" 'e' : Execute all instructions starting from PC.")
    print(" 'p' : Print out register contents.")
    print(" 'r' : Reset processor, clearing all signals, registers and memory.")
    print(" 'd' : Enable dump content from processor.")
    print(" 'c' : Choose endianess.")
    print(" 'x' : Exit program.")

def print_error(message = "ERROR!"):
    print(f"[!] {message}")

def check_file_path_is_bin(file_path):
    if os.path.exists(file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension == ".bin":                    
            return True
        else:
            print_error("File found, but file extension is not '.bin'!")
            return False
    else:
        print_error("File not found!")
        return False

def main():
    # Placeholders until file is parsed
    proc = None
    file_path = ""
    dump_enabled = False
    little_endian = True
    
    print_intro()
    print_help_menu()
        
    while True:
        user_input = input("Your input: ")
        
        if user_input == 'h':
            print_help_menu()            
        
        if user_input == 'f':
            file_path = input("Please enter file path : ")
            
            if check_file_path_is_bin(file_path):
                proc = Processor(file_path = file_path)
                print("Program loaded successfully from: '%s'!" % os.path.basename(file_path).split('/')[-1])
        
        if user_input == 's':
            if proc == None:
                print_error("Program not yet loaded, please provide a path to a binary file.")
            
            elif (proc.pc.get_addr() > (len(proc.imem.mem_slot))) | (proc.dec.get_opcode() == const.I_TYPE_ENV):
                print_error("Program already fully executed! Parse a new file via 'f' or restart via 'r'.")
            
            else:
                proc.execute_step(do_print = dump_enabled)          
                            
        if user_input == 'e':
            if proc == None:
                print_error("Program not yet loaded, please provide a path to a binary file.")
            
            elif (proc.pc.get_addr() > (len(proc.imem.mem_slot))) | (proc.dec.get_opcode() == const.I_TYPE_ENV):
                print_error("Program already fully executed! Parse a new file via 'f' or restart via 'r'.")
                
            else:
                proc.execute_program(do_print = dump_enabled)
                if dump_enabled:
                    proc.print_register_content(repr = 'hex')

        if user_input == 'p':
            if proc == None:
                print_error("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc.print_register_content(repr = 'hex', little_endian = little_endian)

        if user_input == 'r':
            if proc == None:
                print_error("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc = Processor(file_path = file_path)
        
        if user_input == 'd':
            while True:
                user_choice = input("Enable dump ['e'] or Disable dump ['d']: ")
                if user_choice == 'e':
                    dump_enabled = True
                    print("Enabled dump!")
                    break
                elif user_choice == 'd':
                    dump_enabled = False
                    print("Disabled dump!")
                    break
                else:
                    print_error("Input was not 'e' or 'd'!")
        
        if user_input == 'c':
            while True:
                user_choice = input("Little Endian ['l'] or Big Endian ['b']: ")
                if user_choice == 'l':
                    little_endian = True
                    print("Little Endian chosen!")
                    break
                elif user_choice == 'b':
                    little_endian = False
                    print("Big Endian chosen!")
                    break
                else:
                    print_error("Input was not 'l' or 'b'!")

        if user_input == 'x':
            print("Closing simulation, bye!")
            break

        if user_input not in ['h', 's', 'f', 'e', 'p', 'r', 'd', 'c', 'x']:
            print_error("Invalid input, try again!")

if __name__ == "__main__":
    main()