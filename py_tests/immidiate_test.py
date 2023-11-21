import pytest
import src.immidiate as imm
import src.signal_constants as const

class Test_Immidiate(object):

    imm = None

    opcodes = [const.R_TYPE, const.I_TYPE, const.S_TYPE, const.B_TYPE, const.U_TYPE_LOAD, const.U_TYPE_ADD, const.J_TYPE]
    func7   = [0b0000000,   0b0001010,  0b1000000,  0b1111111]
    reg_2   = [0b00000,     0b01010,    0b10100,    0b11111]
    reg_1   = [0b00000,     0b00101,    0b10000,    0b11111]
    rd      = [0b00000,     0b00101,    0b10001,    0b11111]
    func3   = [0b000,       0b001,      0b100,      0b111]

    
    test_inputs = list(zip(func7, reg_2, reg_1, rd, func3))
    
    all_inputs = []
    for i in range(len(opcodes)):
        for j in range(len(test_inputs)):
            all_inputs.append((opcodes[i],) + test_inputs[j])
    
    #           R   I               S               B                   U_load                              U_add                               J          
    expected = [0,  0,              0,              0,                  0,                                  0,                                  0,
                0,  0b000101001010, 0b000101000101, 0b0100101000100,    0b00010100101000101001000000000000, 0b00010100101000101001000000000000, 0b000101001000101001010,
                0,  0b100000010100, 0b100000010001, 0b1100000010000,    0b10000001010010000100000000000000, 0b10000001010010000100000000000000, 0b110000100000000010100,
                0,  0b111111111111, 0b111111111111, 0b1111111111110,    0b11111111111111111111000000000000, 0b11111111111111111111000000000000, 0b111111111111111111110]
    
    # Decoding expected results:    
    # I Type (func7 & reg_2)
    # 0000000 00000 = 0
    # 0001010 01010 = 330
    # 1000000 10100 = 2068
    # 1111111 11111 = 4095

    # S Type (func7 & rd)
    # 0000000 00000 = 0
    # 0001010 00101 = 325
    # 1000000 10001 = 2065
    # 1111111 11111 = 4095

    # B Type ((func7[6] rd[0] func7[5:0] rd[4:1]) << 1)
    # [0]000000 0000[0] 0 -> [0][0]000000 0000 0 = 0 
    # [0]001010 0010[1] 0 -> [0][1]001010 0010 0 = 0100101000100 = 2372
    # [1]000000 1000[1] 0 -> [1][1]000000 1000 0 = 1100000010000 = 6160
    # [1]111111 1111[1] 0 -> [1][1]111111 1111 0 = 1111111111110 = 8190

    # U Type ((func7 & reg_2 & reg_1 & func3) << 12)
    # 0000000 00000 00000 000 = 0
    # 0001010 01010 00101 001 -> 0001010 01010 00101 001 000000000000 = 346198016
    # 1000000 10100 10000 100 -> 1000000 10100 10000 100 000000000000 = 2168995840
    # 1111111 11111 11111 111 -> 1111111 11111 11111 111 000000000000 = 4294963200

    # J Type ((func7[6] reg_1[4:0] func3[2:0] reg_2[0] func7[5:0] reg_2[4:1]) << 1)
    # [0][000000] [0000[0] [00000 000] [0] -> [0] [00000 000] [0] [000000] [0000] [0] = 0
    # [0][001010] [0101[0] [00101 001] [0] -> [0] [00101 001] [0] [001010] [0101] [0] = 168266
    # [1][000000] [1010[0] [10000 100] [0] -> [1] [10000 100] [0] [000000] [1010] [0] = 1589268
    # [1][111111] [1111[1] [11111 111] [0] -> [1] [11111 111] [1] [111111] [1111] [0] = 2097150

    all_test_parameters = []
    for i in range(len(all_inputs)):
        all_test_parameters.append(all_inputs[i] + (expected[i],))
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.imm = imm.Immidiate()

    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.imm

    def test_get_opcode(self):
        assert self.imm.get_opcode() == 0
    
    @pytest.mark.parametrize("opcode, expected", zip(opcodes,opcodes))
    def test_set_opcode(self, opcode, expected):
        self.imm.set_opcode(opcode)
        assert self.imm.opcode == expected
    
    def test_get_func3(self):
        assert self.imm.get_func3() == 0
    
    @pytest.mark.parametrize("func3, expected", zip(func3,func3))
    def test_set_func3(self, func3, expected):
        self.imm.set_func3(func3)
        assert self.imm.func3 == expected
    
    def test_get_func7(self):
        assert self.imm.get_func7() == 0
    
    @pytest.mark.parametrize("func7, expected", zip(func7,func7))
    def test_set_func7(self, func7, expected):
        self.imm.set_func7(func7)
        assert self.imm.func7 == expected
    
    def test_get_rd(self):
        assert self.imm.get_rd() == 0
    
    @pytest.mark.parametrize("rd, expected", zip(rd,rd))
    def test_set_rd(self, rd, expected):
        self.imm.set_rd(rd)
        assert self.imm.rd == expected
    
    def test_get_reg_1(self):
        assert self.imm.get_reg_1() == 0
    
    @pytest.mark.parametrize("reg_1, expected", zip(reg_1,reg_1))
    def test_set_reg_1(self, reg_1, expected):
        self.imm.set_reg_1(reg_1)
        assert self.imm.reg_1 == expected
    
    def test_get_reg_2(self):
        assert self.imm.get_reg_2() == 0
    
    @pytest.mark.parametrize("reg_2, expected", zip(reg_2,reg_2))
    def test_set_reg_2(self, reg_2, expected):
        self.imm.set_reg_2(reg_2)
        assert self.imm.reg_2 == expected
    
    def test_get_res(self):
        assert self.imm.get_res() == 0
    
    @pytest.mark.parametrize("res, expected", [(0,0), (1,1), (-42,-42), (1234,1234), (0xFFFF,0xFFFF)])
    def test_set_res(self, res, expected):
        self.imm.set_res(res)
        assert self.imm.res == expected

####################################################
    @pytest.mark.parametrize("opcodes, func7, reg_2, reg_1, rd, func3, expected", all_test_parameters)
    def test_print_test_values(self, opcodes, func7, reg_2, reg_1, rd, func3, expected):
        print(opcodes, func7, reg_2, reg_1, rd, func3, expected)
        assert True
####################################################

    def test_execute_r_type(self):
        # TODO
        pass

    def test_execute_i_type(self):
        # TODO
        pass

    def test_execute_s_type(self):
        # TODO
        pass

    def test_execute_b_type(self):
        # TODO
        pass

    def test_execute_u_type(self):
        # TODO
        pass
        
    def test_execute_j_type(self):
        # TODO
        pass

    def test_compute_res(self):
        # TODO
        pass