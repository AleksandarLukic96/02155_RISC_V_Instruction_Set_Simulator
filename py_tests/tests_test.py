import pytest
import src.processor as proc
import src.signal_constants as const
import src.utils as utils
import os

class Test_Processor(object):
    
    proc = None

    dir = os.getcwd()
    file_path_bin = os.path.join(dir, "tests", "bin_files_only") 
    file_path_bins = [
         os.path.join(file_path_bin, "_t1_addlarge.bin")
        ,os.path.join(file_path_bin, "_t1_addneg.bin")
        ,os.path.join(file_path_bin, "_t1_addpos.bin")
        ,os.path.join(file_path_bin, "_t1_bool.bin")
        ,os.path.join(file_path_bin, "_t1_set.bin")
        ,os.path.join(file_path_bin, "_t1_shift.bin")
        ,os.path.join(file_path_bin, "_t1_shift2.bin")
        ,os.path.join(file_path_bin, "_t2_branchcnt.bin")
        ,os.path.join(file_path_bin, "_t2_branchmany.bin")
        ,os.path.join(file_path_bin, "_t2_branchtrap.bin")
        ,os.path.join(file_path_bin, "_t3_loop.bin")
        ,os.path.join(file_path_bin, "_t3_recursive.bin")
        ,os.path.join(file_path_bin, "_t3_string.bin")
        ,os.path.join(file_path_bin, "_t3_width.bin")
        ,os.path.join(file_path_bin, "t1.bin")
        ,os.path.join(file_path_bin, "t2.bin")
        ,os.path.join(file_path_bin, "t3.bin")
        ,os.path.join(file_path_bin, "t4.bin")
        ,os.path.join(file_path_bin, "t5.bin")
        ,os.path.join(file_path_bin, "t6.bin")
        ,os.path.join(file_path_bin, "t7.bin")
        ,os.path.join(file_path_bin, "t8.bin")
        ,os.path.join(file_path_bin, "t9.bin")
        ,os.path.join(file_path_bin, "t10.bin")
        ,os.path.join(file_path_bin, "t11.bin")
        ,os.path.join(file_path_bin, "t12.bin")
        ,os.path.join(file_path_bin, "t13.bin")
        ,os.path.join(file_path_bin, "t14.bin")
        ,os.path.join(file_path_bin, "t15.bin")
    ]
    
    file_path_res = os.path.join(dir, "tests", "res_files_only") 
    file_path_ress = [
         os.path.join(file_path_res, "_t1_addlarge.res")
        ,os.path.join(file_path_res, "_t1_addneg.res")
        ,os.path.join(file_path_res, "_t1_addpos.res")
        ,os.path.join(file_path_res, "_t1_bool.res")
        ,os.path.join(file_path_res, "_t1_set.res")
        ,os.path.join(file_path_res, "_t1_shift.res")
        ,os.path.join(file_path_res, "_t1_shift2.res")
        ,os.path.join(file_path_res, "_t2_branchcnt.res")
        ,os.path.join(file_path_res, "_t2_branchmany.res")
        ,os.path.join(file_path_res, "_t2_branchtrap.res")
        ,os.path.join(file_path_res, "_t3_loop.res")
        ,os.path.join(file_path_res, "_t3_recursive.res")
        ,os.path.join(file_path_res, "_t3_string.res")
        ,os.path.join(file_path_res, "_t3_width.res")
        ,os.path.join(file_path_res, "t1.res")
        ,os.path.join(file_path_res, "t2.res")
        ,os.path.join(file_path_res, "t3.res")
        ,os.path.join(file_path_res, "t4.res")
        ,os.path.join(file_path_res, "t5.res")
        ,os.path.join(file_path_res, "t6.res")
        ,os.path.join(file_path_res, "t7.res")
        ,os.path.join(file_path_res, "t8.res")
        ,os.path.join(file_path_res, "t9.res")
        ,os.path.join(file_path_res, "t10.res")
        ,os.path.join(file_path_res, "t11.res")
        ,os.path.join(file_path_res, "t12.res")
        ,os.path.join(file_path_res, "t13.res")
        ,os.path.join(file_path_res, "t14.res")
        ,os.path.join(file_path_res, "t15.res")
    ]
    
    @pytest.mark.parametrize("file_path_bin, file_path_res", zip(file_path_bins, file_path_ress))
    def test_compare_result(self, file_path_bin, file_path_res):
        print(f"Setting up {self}")
        self.proc = proc.Processor(file_path = file_path_bin, mem_size = const.MiB)
        expected_result = utils.prepare_result(file_path = file_path_res, little_endian = False)
        
        self.proc.execute_program()
        
        regs = self.proc.regs.regs
        
        assert regs == expected_result
