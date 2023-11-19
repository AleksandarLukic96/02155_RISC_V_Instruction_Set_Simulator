import pytest
import src.instructionMemory as imem
import numpy as np

class Test_InstructionMemory(object):

    imem = None

    file_path = "./tests/task1/addlarge.bin"
    
    file_path_task_1 = ["./tests/task1/addlarge.bin", "./tests/task1/addneg.bin", "./tests/task1/addpos.bin", "./tests/task1/bool.bin", "./tests/task1/set.bin", "./tests/task1/shift.bin", "./tests/task1/shift2.bin"]
    file_path_task_2 = ["./tests/task2/branchcnt.bin", "./tests/task2/branchmany.bin", "./tests/task2/branchtrap.bin"]
    file_path_task_3 = ["./tests/task3/loop.bin", "./tests/task3/recursive.bin", "./tests/task3/string.bin", "./tests/task3/width.bin"]
    file_path_task_4 = ["./tests/task4/t1.bin", "./tests/task4/t2.bin", "./tests/task4/t3.bin", "./tests/task4/t4.bin", "./tests/task4/t5.bin", "./tests/task4/t6.bin", "./tests/task4/t7.bin", "./tests/task4/t8.bin", "./tests/task4/t9.bin", "./tests/task4/t10.bin", "./tests/task4/t11.bin", "./tests/task4/t12.bin", "./tests/task4/t13.bin", "./tests/task4/t14.bin", "./tests/task4/t15.bin"]
    file_path_task_all = []
    file_path_task_all.extend(file_path_task_1)
    file_path_task_all.extend(file_path_task_2)
    file_path_task_all.extend(file_path_task_3)
    file_path_task_all.extend(file_path_task_4)
    file_path_task_all.append("invalid_path")
     
    @pytest.fixture(autouse=True)
    def setup_class(self):
        print(f"Setting up {self}")
        self.imem = imem.InstructionMemomry(file_path = self.file_path_task_1[0], addr = 0)
        
    def teardown_class(self):
        print(f"Tearing down {self}")
        del self.imem

    @pytest.mark.xfail(reason = "Invalid path given. This is expected.")
    @pytest.mark.parametrize("file_path", file_path_task_all)
    def test_init(self, file_path):
        im = imem.InstructionMemomry(file_path = file_path)
        assert (
            (im.addr == 0) 
            & (im.number_of_insts == len(im.data) // 4)
            )

    @pytest.mark.parametrize("addr, expected", [(0, 0), (4, 4), (0xFFFFFFFF, 0xFFFFFFFF)])
    def test_set_addr(self, addr, expected):
        self.imem.set_addr(addr)
        assert self.imem.addr == expected
    
    def test_get_addr(self):
        assert self.imem.get_addr() == 0

    @pytest.mark.parametrize("addr, expeted", [(0, 0x80000537), (4, 0x00150513), (8, 0x800005b7), (12, 0xffe58593), (16, 0x00b50633), (20, 0x00a00893), (24, 0x00000073), (28, 0x00000004), (32, 0x00000014), (36, 0x00000003), (40, 0x00554e47), (44, 0xc9ce871c), (48, 0x44089d5d), (52, 0x7d6f3231), (56, 0x2788044c), (60, 0x3a48c48e)])
    def test_fetch_inst_at_addr(self, addr, expeted):  
        self.imem.addr = addr
        assert self.imem.fetch_inst_at_addr() == expeted