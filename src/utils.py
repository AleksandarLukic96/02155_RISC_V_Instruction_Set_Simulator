# Represent numeric values as Binary, Hex or Integer and return as a string
def to_str_bin(val):
    str = "{0:032b}".format(val % (1<<32))
    return "0b%s" % (str.upper())

def to_str_hex(val):
    str = "{0:08x}".format(val % (1<<32))
    return "0x%s" % (str.upper())

def to_str_int(val):
    return "{0:12}".format(val)

def to_str_int_hex_bin(val):
    return to_str_int(val) + " " + to_str_hex(val) + " " + to_str_bin(val)

def sign_extend(num, msb_pos = 16):  # Always 32 bits values
    if (msb_pos <= 0) | (msb_pos > 32):
        return 0
    
    # Placeholder for result
    sign_extension_mask = 0x0
    res = 0x0

    # Find sign mask according to number of bits        
    sign_mask = 0b1 << msb_pos - 1 
    
    # Extract signed bit accroding to number of bits
    signed_bit = (num & sign_mask) >> (msb_pos - 1)
    
    # Extend according to signed bit
    if signed_bit == 1:
        sign_extension = 0x1
    else:
        sign_extension = 0x0
        
    for i in range(32 - msb_pos):
        sign_extension_mask = sign_extension_mask | (sign_extension << i)

    sign_extension_mask = sign_extension_mask << msb_pos
        
    res = sign_extension_mask | num
    return res

def remove_overflow(num):
    return num & 0x00000000FFFFFFFF

def prepare_result(file_path, little_endian = True):
    # Load bin file into pyton
    f = open(file_path, mode = "rb")
    
    # Reading file data with read() method
    data = f.read()
    
    # If False, then read bytes in big endian order
    little_endian = little_endian
    
    # Concatinate bytes into 32-bit instructions as int-array
    res = []
         
    i = 0   
    if little_endian:
        while i < (len(data)):
            res.append(
             (data[i + 0] << 24)
            |(data[i + 1] << 16)
            |(data[i + 2] <<  8)
            |(data[i + 3] <<  0)
            )
            i += 4
    else:
        while i < (len(data)):
            res.append(
             (data[i + 3] << 24)
            |(data[i + 2] << 16)
            |(data[i + 1] <<  8)
            |(data[i + 0] <<  0)
            )
            i += 4
    
    # Closing the opened file
    f.close()
    
    return res

def convert_endianess(data):
    # Reverse the byte order of the data to the opposite endian
    res = []
    
    i = 0   
    while i < (len(data)):
        res.append(
            ((data[i] & 0x000000FF) << 24)
            |((data[i] & 0x0000FF00) <<  8)
            |((data[i] & 0x00FF0000) >>  8)
            |((data[i] & 0xFF000000) >> 24)
            )
        i += 1
    return res

def convert_to_bytearray(data, little_endian = True):
    b_arr = bytearray()
    
    if little_endian == False:
        data = convert_endianess(data)
    
    i = 0   
    while i < (len(data)):
        b_arr.append((data[i] & 0x000000FF) >>  0)
        b_arr.append((data[i] & 0x0000FF00) >>  8)
        b_arr.append((data[i] & 0x00FF0000) >> 16)
        b_arr.append((data[i] & 0xFF000000) >> 24)
        i += 1
    
    return b_arr

def list_to_bin_file(data, file_path, little_endian = True):
    # move into subfolder "exports"
    file_path = file_path.replace('/tests/bin_files_only/', '/exports/')
    
    print(file_path)
    # Convert data to bytearray
    b_arr = convert_to_bytearray(data = data, little_endian = little_endian)
    
    # Create or overwrite bin file with export data
    with open(file_path, "wb") as file:
        file.write(b_arr)
    
    file.close()
