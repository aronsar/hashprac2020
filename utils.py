def load_input_file(input_file_path):
    input_file = open(input_file_path, 'r')

    (target, total_pizzas) = input_file.readline().strip().split(' ')
    slice_arr = input_file.readline().strip().split(' ')

    return (int(target), int(total_pizzas), slice_arr)
    
def write_output_file(idx_array):
    pass
