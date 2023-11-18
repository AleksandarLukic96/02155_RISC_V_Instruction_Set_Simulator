import pytest
import src.programCounter as pc

class Test_ProgramCounter:
    
    pc = None

    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.pc = pc.ProgramCounter()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.pc
    
    def test_init(self):
        assert self.pc.addr == 0
    
    @pytest.mark.parametrize("addr, expected", [(0, 0), (1, 1), (4, 4), (-12, -12)])
    def test_set_addr(self, addr, expected):
        self.pc.set_addr(addr)
        assert self.pc.addr == expected
    
    def test_get_addr(self):
        assert self.pc.get_addr() == 0