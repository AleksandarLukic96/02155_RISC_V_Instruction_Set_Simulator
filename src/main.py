import os
from processor import Processor

def print_intro():
    width = 50
    str_1 = '{: ^{width}}'.format("RISC-V Single Cycle Instruction Set Simulation", width = width)
    str_2 = '{: ^{width}}'.format("This program loads a given binary file,", width = width)
    str_3 = '{: ^{width}}'.format("and interprets it as a RISC-V program.", width = width)
    str_0 = "#" * width
    print(f"##{str_0}##")
    print(f"##{str_1}##")
    print(f"##{str_2}##")
    print(f"##{str_3}##")
    print(f"##{str_0}##")

def print_help_menu():
    print("Help Menu: ")
    print(" 'h' : Print out actions to terminal.")
    print(" 'c' : Provide file path to binary file.")
    print(" 's' : Execute current instruction at PC.")
    print(" 'e' : Execute all instructions starting from PC.")
    print(" 'p' : Print out register contents.")
    print(" 'r' : Reset processor, clearing all signals, registers and memory.")
    print(" 'x' : Exit program.")

def check_file_path_is_bin(file_path):
    if os.path.exists(file_path):
        _, file_extension = os.path.splitext(file_path)
        if file_extension == ".bin":                    
            return True
        else:
            print(" File found, but file extension is not '.bin'!")
            return False
    else:
        print(" File not found!")
        return False

def main():
    # Placeholders until file is parsed
    proc = None
    file_path = ""
    
    print_intro()
    print_help_menu()
        
    while True:
        user_input = input("Your input: ")
        
        if user_input == 'h':
            print_help_menu()            
        
        if user_input == 's':
            if proc == None:
                print("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc.execute_step()            
        
        if user_input == 'c':
            file_path = input("Please enter file path : ")
            
            if check_file_path_is_bin(file_path):
                proc = Processor(file_path = file_path)
                print(" Program loaded successfully!")
                    
        if user_input == 'e':
            if proc == None:
                print("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc.execute_program(do_print = True)

        if user_input == 'p':
            if proc == None:
                print("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc.print_register_content(repr = 'hex')

        if user_input == 'r':
            if proc == None:
                print("Program not yet loaded, please provide a path to a binary file.")
            else:
                proc = Processor(file_path = file_path)

        if user_input == 'x':
            print("Closing simulation, bye!")
            break

        if user_input not in ['h', 's', 'c', 'e', 'p', 'r', 'x']:
            print("Invalid input, try again!")

if __name__ == "__main__":
    main()