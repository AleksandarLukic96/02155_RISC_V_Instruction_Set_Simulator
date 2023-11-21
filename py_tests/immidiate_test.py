import pytest
import src.immidiate as imm
import src.signal_constants as const

class Test_Immidiate(object):

    imm = None

    opcodes = [const.R_TYPE, const.I_TYPE, const.S_TYPE, const.B_TYPE, const.J_TYPE]
    func3   = [0b000,       0b001,      0b100,      0b111]
    func7   = [0b0000000,   0b0001010,  0b1000000,  0b1111111]
    rd      = [0b00000,     0b00101,    0b10001,    0b11111]
    reg_1   = [0b00000,     0b00101,    0b10000,    0b11111]
    reg_2   = [0b00000,     0b01010,    0b10100,    0b11111]
    
    all_inputs = list(zip(func3, func7, rd, reg_1, reg_2))
    
    test_values = []
    for i in range(len(opcodes)):
        for j in range(len(all_inputs)):
            test_values.append((opcodes[i],) + all_inputs[j])
    
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
    @pytest.mark.parametrize("opcodes, func3, func7, rd, reg_1, reg_2", test_values)
    def test_print_test_values(self, opcodes, func3, func7, rd, reg_1, reg_2):
        print(opcodes, func3, func7, rd, reg_1, reg_2)
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