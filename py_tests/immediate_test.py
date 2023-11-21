import pytest
import src.immediate as imm
import src.signal_constants as const

class Test_Immediate(object):

    imm = None

    opcodes = [const.R_TYPE, const.I_TYPE, const.S_TYPE, const.B_TYPE, const.U_TYPE_LOAD, const.U_TYPE_ADD, const.J_TYPE]
    func7s  = [0b0000000,   0b0001010,  0b1000000,  0b1111111]
    reg_2s  = [0b00000,     0b01010,    0b10100,    0b11111]
    reg_1s  = [0b00000,     0b00101,    0b10000,    0b11111]
    func3s  = [0b000,       0b001,      0b100,      0b111]
    rds     = [0b00000,     0b00101,    0b10001,    0b11111]

    
    test_inputs = list(zip(func7s, reg_2s, reg_1s, func3s, rds))
    
    all_inputs = []
    for i in range(len(opcodes)):
        for j in range(len(test_inputs)):
            all_inputs.append((opcodes[i],) + test_inputs[j])
    
    expected = [
        0, 0, 0, 0, # R
        0, 0b000101001010, 0b100000010100, 0b111111111111, # I
        0, 0b000101000101, 0b100000010001, 0b111111111111, # S
        0, 0b0100101000100, 0b1100000010000, 0b1111111111110, # B
        0, 0b00010100101000101001000000000000, 0b10000001010010000100000000000000, 0b11111111111111111111000000000000, # U_load
        0, 0b00010100101000101001000000000000, 0b10000001010010000100000000000000, 0b11111111111111111111000000000000, # U_add
        0, 0b000101001000101001010, 0b110000100000000010100, 0b111111111111111111110 # J
    ]

    all_test_parameters = []
    for i in range(len(all_inputs)):
        all_test_parameters.append(all_inputs[i] + (expected[i],))
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.imm = imm.Immediate()

    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.imm

    @pytest.mark.parametrize("func7, expected", zip(func7s, func7s))
    def test_set_func7(self, func7, expected):
        self.imm.set_func7(func7)
        assert self.imm.func7 == expected
    
    def test_get_func7(self):
        assert self.imm.get_func7() == 0
    
    @pytest.mark.parametrize("reg_2, expected", zip(reg_2s, reg_2s))
    def test_set_reg_2(self, reg_2, expected):
        self.imm.set_reg_2(reg_2)
        assert self.imm.reg_2 == expected
    
    def test_get_reg_2(self):
        assert self.imm.get_reg_2() == 0
    
    @pytest.mark.parametrize("reg_1, expected", zip(reg_1s, reg_1s))
    def test_set_reg_1(self, reg_1, expected):
        self.imm.set_reg_1(reg_1)
        assert self.imm.reg_1 == expected
    
    def test_get_reg_1(self):
        assert self.imm.get_reg_1() == 0

    @pytest.mark.parametrize("func3, expected", zip(func3s, func3s))
    def test_set_func3(self, func3, expected):
        self.imm.set_func3(func3)
        assert self.imm.func3 == expected
    
    def test_get_func3(self):
        assert self.imm.get_func3() == 0    
    
    @pytest.mark.parametrize("rd, expected", zip(rds, rds))
    def test_set_rd(self, rd, expected):
        self.imm.set_rd(rd)
        assert self.imm.rd == expected

    def test_get_rd(self):
        assert self.imm.get_rd() == 0
    
    @pytest.mark.parametrize("opcode, expected", zip(opcodes, opcodes))
    def test_set_opcode(self, opcode, expected):
        self.imm.set_opcode(opcode)
        assert self.imm.opcode == expected
    
    def test_get_opcode(self):
        assert self.imm.get_opcode() == 0
        
    @pytest.mark.parametrize("res, expected", [(0,0), (1,1), (-42,-42), (1234,1234), (0xFFFF,0xFFFF)])
    def test_set_res(self, res, expected):
        self.imm.set_res(res)
        assert self.imm.res == expected

    def test_get_res(self):
        assert self.imm.get_res() == 0

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[0:4])
    def test_execute_r_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.execute_r_type()
        assert self.imm.res == expected 

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[4:8])
    def test_execute_i_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3        
        self.imm.execute_i_type()
        assert self.imm.res == expected 

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[8:12])
    def test_execute_s_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.execute_s_type()
        assert self.imm.res == expected

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[12:16])
    def test_execute_b_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.execute_b_type()
        assert self.imm.res == expected

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[16:24])
    def test_execute_u_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.execute_u_type()
        assert self.imm.res == expected

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters[24:28])
    def test_execute_j_type(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.execute_j_type()
        assert self.imm.res == expected

    @pytest.mark.parametrize("opcode, func7, reg_2, reg_1, func3, rd, expected", all_test_parameters)
    def test_compute_res(self, opcode, func7, reg_2, reg_1, func3, rd, expected):
        self.imm.opcode = opcode
        self.imm.func7 = func7
        self.imm.reg_2 = reg_2
        self.imm.reg_1 = reg_1
        self.imm.rd = rd
        self.imm.func3 = func3
        self.imm.compute_res()
        assert self.imm.res == expected