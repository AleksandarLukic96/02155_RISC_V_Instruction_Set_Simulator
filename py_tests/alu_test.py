import pytest
import src.alu as alu

ADD  = 0b00000 # 0
SLL  = 0b00001 # 1
XOR  = 0b00100 # 4
OR   = 0b00110 # 6
AND  = 0b00111 # 7
SRL  = 0b00101 # 5
SUB  = 0b01000 # 8
SRA  = 0b01101 # 13
SLT  = 0b00010 # 2
SLTU = 0b00011 # 3

class Test_ALU:
    
    alu = None
    
    alu_ctrl = [ADD, SLL, XOR, OR, AND, SRL, SUB, SRA, SLT, SLTU]
    alu_ctrl_double = list(zip(alu_ctrl, alu_ctrl))
    alu_ctrl_quad = [ADD, ADD, ADD, ADD, 
                     SLL, SLL, SLL, SLL, 
                     XOR, XOR, XOR, XOR,
                     OR, OR, OR, OR,
                     AND, AND, AND, AND,
                     SRL, SRL, SRL, SRL, 
                     SUB, SUB, SUB, SUB, 
                     SRA, SRA, SRA, SRA,
                     SLT, SLT, SLT, SLT,
                     SLTU, SLTU, SLTU, SLTU]
    
    alu_op_1 = [0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4,
                0, 4, 4, -4]
    
    alu_op_2 = [0, 11, -11, -11,
                0, 11, -11, -11,
                0, 11, -11, -11,
                0, 11, -11, -11,
                0, 11, -11, -11,
                0, 1, -1, -1,
                0, 11, -11, -11,
                0, 1, -1, -1,
                0, 11, -11, -11,
                0, 11, -11, -11]
    
    res = [0, 15, -7, -15,
           0, 8192, 0, 0,
           0, 15, -15, 9,
           0, 15, -11, -3,
           0, 0, 4, -12,
           0, 2, 0, 0,
           0, -7, 15, 7,
           0, 2, 0, -1,
           0, 1, 0, 0,
           0, 1, 1, 0]
    
    compute_test_values = list(zip(alu_ctrl_quad, alu_op_1, alu_op_2, res))
    
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.alu = alu.ALU()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.alu
    
    def test_init(self):
        assert (
            (self.alu.ctrl == 0)
            & (self.alu.op_1 == 0)
            & (self.alu.op_2 == 0)
            & (self.alu.res == 0)
        )
    
    @pytest.mark.parametrize("ctrl, expected", alu_ctrl_double)
    def test_set_ctrl(self, ctrl, expected):
        self.alu.set_ctrl(ctrl)
        assert self.alu.ctrl == expected
    
    def test_get_ctrl(self):
        assert self.alu.get_ctrl() == 0

    @pytest.mark.parametrize("op_1, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_op_1(self, op_1, expected):
        self.alu.set_op_1(op_1)
        assert self.alu.op_1 == expected
    
    def test_get_op_1(self):
        assert self.alu.get_op_1() == 0

    @pytest.mark.parametrize("op_2, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_op_2(self, op_2, expected):
        self.alu.set_op_2(op_2)
        assert self.alu.op_2 == expected
    
    def test_get_op_2(self):
        assert self.alu.get_op_2() == 0
    
    @pytest.mark.parametrize("res, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_res(self, res, expected):
        self.alu.set_res(res)
        assert self.alu.res == expected
    
    def test_get_res(self):
        assert self.alu.get_res() == 0
    
    @pytest.mark.skip(reason = "Need fixing of shift operations!")
    @pytest.mark.parametrize("ctrl, op_1, op_2, expected", compute_test_values)
    def test_copmute_res(self, ctrl, op_1, op_2, expected):
        self.alu.ctrl = ctrl
        self.alu.op_1 = op_1
        self.alu.op_2 = op_2
        self.alu.compute_res()
        assert self.alu.get_res() == expected
    
    @pytest.mark.parametrize("ctrl, op_1, op_2, expected", [(ADD,0,0,0), (ADD,4,11,15), (ADD,4,-11,-7), (ADD, -4, -11, -15)])
    def test_copmute_res_add(self, ctrl, op_1, op_2, expected):
        self.alu.ctrl = ctrl
        self.alu.op_1 = op_1
        self.alu.op_2 = op_2
        self.alu.compute_res()
        assert self.alu.get_res() == expected