import argparse 
import utils
import tester
#from dp_solution import dp_solution
from hybrid_solution import hybrid_solution
from dp.pdp import dp as pdp # python dp solution
from dp.dp import dp as cdp # cython dp solution
from time import time
import numpy as np

parser = argparse.ArgumentParser() 
parser.add_argument(
    '--input_file', 
    type=str, 
    default='c_medium.in', 
    help='relative path of input file') 
parser.add_argument(
    '--dp_limit', 
    type=int, 
    default=10000000000, 
    help='the max size of the dynamic programming table') 
args = parser.parse_args()


if __name__ == '__main__':
    target, total_pizzas, slice_arr = utils.load_input_file(args.input_file)
    if target * total_pizzas < args.dp_limit:
        t = time()
        idx_arr = pdp(slice_arr, target)
        print("Python dp took " + str(time()-t))

        t = time()

        slice_arr = np.array(slice_arr, dtype=np.int32) # needed for cython
        idx_arr = cdp(slice_arr, target)
        print("Cython dp took " + str(time()-t))
        
    else:
        idx_arr = hybrid_solution(slice_arr, target)
    
    tester.test_solution(target, total_pizzas, slice_arr, idx_arr)
    utils.write_output_file(idx_arr, args.input_file)
