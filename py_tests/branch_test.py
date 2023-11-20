import pytest
import src.branch as branch
import src.signal_constants as const

class Test_Branch(object):
    
    branch = None
    
    branch_ctrl = [const.BEQ, const.BNE, const.BLT, const.BGE, const.BLTU, const.BGEU]
    branch_ctrl_double = list(zip(branch_ctrl, branch_ctrl))
    branch_ctrl_triple = [const.BEQ, const.BEQ, const.BEQ, const.BEQ, const.BNE, const.BNE, const.BNE, const.BNE, const.BLT, const.BLT, const.BLT, const.BLT, const.BGE, const.BGE, const.BGE, const.BGE, const.BLTU, const.BLTU, const.BLTU, const.BLTU, const.BGEU, const.BGEU, const.BGEU, const.BGEU]
    val_1 =     [0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4, 0, 2, 0, 4]
    val_2 =     [0, 0, 3, 4, 0, 0, 3, 4, 0, 0, 3, 4, 0, 0, 3, 4, 0, 0, 3, 4, 0, 0, 3, 4]
    expected =  [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    branch_ctrl_expected = list(zip(branch_ctrl_triple, val_1, val_2, expected))
        
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.branch = branch.Branch()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.branch

    @pytest.mark.parametrize("op_1, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_op_1(self, op_1, expected):
        self.branch.set_op_1(op_1)
        assert self.branch.op_1 == expected 
    
    def test_get_op_1(self):
        assert self.branch.get_op_1() == 0
    
    @pytest.mark.parametrize("op_2, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_op_2(self, op_2, expected):
        self.branch.set_op_2(op_2)
        assert self.branch.op_2 == expected 
    
    def test_get_op_2(self):
        assert self.branch.get_op_2() == 0
    
    @pytest.mark.parametrize("branch_ctrl, expected", branch_ctrl_double)
    def test_set_branch_ctrl(self, branch_ctrl, expected):
        self.branch.set_branch_ctrl(branch_ctrl)
        assert self.branch.branch_ctrl == expected 
    
    @pytest.mark.parametrize("branch_ctrl, expected", branch_ctrl_double)
    def test_get_branch_ctrl(self, branch_ctrl, expected):
        self.branch.branch_ctrl = branch_ctrl
        assert self.branch.get_branch_ctrl() == expected
    
    @pytest.mark.parametrize("branch_taken, expected", [(0, 0), (1, 1)])
    def test_set_branch_taken(self, branch_taken, expected):
        self.branch.set_branch_taken(branch_taken)
        assert self.branch.branch_taken == expected

    def test_get_branch_taken(self):
        assert self.branch.get_branch_taken() == 0

    def test_branch_taken_enable(self):
        self.branch.branch_taken_enable()
        assert self.branch.branch_taken == 1
    
    def test_branch_taken_disable(self):
        self.branch.branch_taken_disable()
        assert self.branch.branch_taken == 0

    @pytest.mark.parametrize("branch_ctrl, op_1, op_2, expected", branch_ctrl_expected)
    def test_compute_branch_taken(self, branch_ctrl, op_1, op_2, expected):
        self.branch.branch_ctrl = branch_ctrl
        self.branch.op_1 = op_1
        self.branch.op_2 = op_2
        self.branch.compute_branch_taken()
        assert self.branch.branch_taken == expected
        