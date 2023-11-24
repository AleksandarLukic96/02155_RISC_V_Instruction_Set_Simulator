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

def sign_extend(num, n_bits = 16):
    n_bits = n_bits
    
    # Placeholder for result
    sign_extension_mask = 0x0
    res = 0x0
    
    # Number of bytes used for storing input
    n_bytes = n_bits // 4

    # Find sign mask according to number of bits        
    sign_mask = 0x8 << ((n_bytes - 1) * 4)
    
    # Extract signed bit accroding to number of bits
    signed_bit = (num & sign_mask) >> (n_bits - 1)
    
    # Extend according to signed bit
    if signed_bit == 1:
        sign_extension = 0xF
    else:
        sign_extension = 0x0
        
    for i in range(8 - n_bytes): # Always 32 bits / 8 bytes result
        sign_extension_mask = sign_extension_mask | (sign_extension << (i*4))

    sign_extension_mask = sign_extension_mask << n_bits
        
    res = sign_extension_mask | num
    return res

def remove_overflow(num):
    return num & 0x00000000FFFFFFFF
