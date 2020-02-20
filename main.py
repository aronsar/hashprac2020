import argparse 
import utils
from dp_solution import dp_solution
from hybrid_solution import hybrid_solution


parser = argparse.ArgumentParser() 
parser.add_argument(
    '--input_file', 
    type=str, 
    default='input/c_medium.in', 
    help='relative path of input file') 
parser.add_argument(
    '--dp_limit', 
    type=int, 
    default=1000, 
    help='the max size of the dynamic programming table') 
args = parser.parse_args()


if __name__ == '__main__':
    target, total_pizzas, slice_arr = utils.load_input_file(args.input_file)

    if target * total_pizzas < args.dp_limit:
        idx_arr = dp_solution(slice_arr, target)

    else:
        idx_arr = hybrid_solution(slice_arr, target)

    utils.write_output_file(idx_arr)
