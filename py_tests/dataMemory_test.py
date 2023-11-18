import pytest
import src.dataMemory as dmem
import numpy as np

class Test_DataMemory(object):

    dmem = dmem.DataMemory()

    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.dmem = dmem.DataMemory(mem_size = 1024)
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.dmem

    def test_init(self):
        assert (
            (self.dmem.mem_size == 1024) 
            & (not np.any(self.dmem.mem_addrs) == True)
            & (len(self.dmem.mem_addrs) == self.dmem.mem_size // 4)
            & (self.dmem.addr == 0) 
            & (self.dmem.data_in == 0) 
            & (self.dmem.data_out == 0) 
            & (self.dmem.write_enabled == 0) 
            & (self.dmem.read_enabled == 0)
            )
    
    @pytest.mark.parametrize("addr, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_addr(self, addr, expected):
        self.dmem.set_addr(addr)
        assert self.dmem.addr == expected
    
    def test_get_addr(self):
        assert self.dmem.get_addr() == 0
    
    @pytest.mark.parametrize("data_in, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_data_in(self, data_in, expected):
        self.dmem.set_data_in(data_in)
        assert self.dmem.data_in == expected
    
    def test_get_data_in(self):
        assert self.dmem.get_data_in() == 0
    
    @pytest.mark.parametrize("data_out, expected", [(0, 0), (1, 1), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_data_out(self, data_out, expected):
        self.dmem.set_data_out(data_out)
        assert self.dmem.data_out == expected
    
    def test_get_data_out(self):
        assert self.dmem.get_data_out() == 0
    
    @pytest.mark.parametrize("val, expected", [(0, 0), (1, 1), (42, 42)])
    def test_set_write_enabled(self, val, expected):
        self.dmem.set_write_enabled(val)
        assert self.dmem.write_enabled == expected

    def test_get_write_enabled(self):
        assert self.dmem.get_write_enabled() == 0
    
    def test_write_enable(self):
        self.dmem.write_enable()
        assert self.dmem.write_enabled == 1
    
    def test_write_disable(self):
        self.dmem.write_disable()
        assert self.dmem.write_enabled == 0
    ########
    @pytest.mark.parametrize("val, expected", [(0, 0), (1, 1), (42, 42)])
    def test_set_read_enabled(self, val, expected):
        self.dmem.set_read_enabled(val)
        assert self.dmem.read_enabled == expected

    def test_get_read_enabled(self):
        assert self.dmem.get_read_enabled() == 0
    
    def test_read_enable(self):
        self.dmem.read_enable()
        assert self.dmem.read_enabled == 1
    
    def test_read_disable(self):
        self.dmem.read_disable()
        assert self.dmem.read_enabled == 0      

    @pytest.mark.xfail(reason = "If addr given is out of bounds, it should fail.")
    @pytest.mark.parametrize("addr, data_in, write_enabled, expected", 
                             [(0, 0, 0, 0),
                              (0, 123, 0, 0),
                              (0, 123, 1, 123),
                              (42, 123, 1, 123),
                              (255, 123, 1, 123),
                              (256, 123, 1, 123)
                              ])
    def test_write_to_addr(self, addr, data_in, write_enabled, expected):
        self.dmem.addr = addr
        self.dmem.data_in = data_in
        self.dmem.write_enabled = write_enabled 
        
        self.dmem.write_to_addr()
        assert self.dmem.mem_addrs[addr] == expected
    
    @pytest.mark.xfail(reason = "If addr given is out of bounds, it should fail.")
    @pytest.mark.parametrize("addr, data_in, read_enabled, expected", 
                             [(0, 0, 0, 0),
                              (0, 123, 0, 0),
                              (0, 123, 1, 123),
                              (42, 123, 1, 123),
                              (255, 123, 1, 123),
                              (256, 123, 1, 123)
                              ])
    def test_read_to_addr(self, addr, data_in, read_enabled, expected):
        self.dmem.addr = addr
        self.dmem.mem_addrs[addr] = data_in
        self.dmem.read_enabled = read_enabled 
        
        self.dmem.read_from_addr()
        assert self.dmem.mem_addrs[addr] == expected
