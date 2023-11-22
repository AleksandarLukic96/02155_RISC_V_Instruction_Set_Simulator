# Represent numeric values as Binary, Hex or Integer and return as a string
def to_str_bin(val):
    str = "{0:032b}".format(val % (1<<32))
    return "0b%s" % (str.upper())

def to_str_hex(val):
    str = "{0:08x}".format(val % (1<<32))
    return "0x%s" % (str.upper())

def to_str_int(val):
    return "{0:10}".format(val)

def to_str_int_hex_bin(val):
    return to_str_int(val) + " " + to_str_hex(val) + " " + to_str_bin(val)

    