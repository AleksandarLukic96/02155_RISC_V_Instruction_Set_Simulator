import pytest
import src.registers as regs
import numpy as np

class Test_Registers:
    regs = None
    
    valid_registers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
                       10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
                       20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 
                       30, 31]
    
    valid_registers_check = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), 
                       (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), 
                       (20, 20), (21, 21), (22, 22), (23, 23),(24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), 
                       (30, 30), (31, 31), (32, 0), (-1, 0)]
    
    valid_data = [0x00000000, 0x00000001, 0x7FFFFFFF, 0xFFFFFFFF]
    
    valid_content = []
    for i in range(len(valid_registers)):
        for j in range(len(valid_data)):
            valid_content.append((valid_registers[i], valid_data[j], valid_data[j]))
    
    content_check = list(zip(valid_registers, valid_data))
    content_check = list(zip(content_check, valid_data))
    
    valid_data_check = [(0, 0), (-1, -1), (0xFFFFFFFF, -1), (0x1FFFFFFFF, -1), (8589934591, -1), (0x7FFFFFFF, 2147483647), (0x12345678, 305419896)]


        
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.regs = regs.Registers()
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.regs
    
    def test_init(self):
        assert (
            (self.regs.reg_1 == 0)
            & (self.regs.reg_2 == 0)
            & (self.regs.rd == 0)
            & (self.regs.data_in == 0)
            & (self.regs.write_enabled == 0)
            & (not np.any(self.regs.regs) == True)
            & (len(self.regs.regs) == 32)
        )
    
    @pytest.mark.parametrize("reg, expected", valid_registers_check)
    def test_set_reg_1(self, reg, expected):
        self.regs.set_reg_1(reg)
        assert self.regs.reg_1 == expected
    
    def test_get_reg_1(self):
        assert self.regs.get_reg_1() == 0
    
    @pytest.mark.parametrize("reg, expected", valid_registers_check)
    def test_set_reg_2(self, reg, expected):
        self.regs.set_reg_2(reg)
        assert self.regs.reg_2 == expected
    
    def test_get_reg_2(self):
        assert self.regs.get_reg_2() == 0
    
    @pytest.mark.parametrize("reg, expected", valid_registers_check)
    def test_set_rd(self, reg, expected):
        self.regs.set_rd(reg)
        assert self.regs.rd == expected
    
    def test_get_rd(self):
        assert self.regs.get_rd() == 0

    @pytest.mark.parametrize("data_in, expected", valid_data_check)
    def test_set_data_in(self, data_in, expected):
        self.regs.set_data_in(data_in)
        assert self.regs.data_in == expected
    
    def test_get_data_in(self):
        assert self.regs.get_data_in() == 0 
    
    @pytest.mark.parametrize("val, expected", [(0, 0), (1, 1), (42, 42)])
    def test_set_write_enabled(self, val, expected):
        self.regs.set_write_enabled(val)
        assert self.regs.write_enabled == expected

    def test_get_write_enabled(self):
        assert self.regs.get_write_enabled() == 0
    
    def test_write_enable(self):
        self.regs.write_enable()
        assert self.regs.write_enabled == 1
    
    def test_write_disable(self):
        self.regs.write_disable()
        assert self.regs.write_enabled == 0


    @pytest.mark.parametrize("reg, data, expected", valid_content)
    def test_return_reg_1_content(self, reg, data, expected):
        self.regs.reg_1 = reg
        self.regs.regs[reg] = data
        assert self.regs.return_reg_1_content() == expected
        
    @pytest.mark.parametrize("reg, data, expected", valid_content)
    def test_return_reg_2_content(self, reg, data, expected):
        self.regs.reg_2 = reg
        self.regs.regs[reg] = data
        assert self.regs.return_reg_2_content() == expected

    @pytest.mark.parametrize("rd, write_enabled, data_in, expected", [(0, 0, 0, 0), (0, 1, 0, 0), (0, 1, 123, 0), (0, 0, 123, 0),
                                                                      (12, 0, 0, 0), (12, 1, 0, 0), (12, 1, 123, 123), (12, 0, 123, 0),
                                                                      (31, 0, 0, 0), (31, 1, 0, 0), (31, 1, 123, 123), (31, 0, 123, 0)])
    def test_write_to_rd(self, rd, write_enabled, data_in, expected):
        self.regs.rd = rd
        self.regs.write_enabled = write_enabled
        self.regs.data_in = data_in
        self.regs.write_to_rd()
        assert self.regs.regs[rd] == expected
