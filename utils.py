from pathlib import Path

def load_input_file(input_file_path):
    input_file = open("inputs/"+ str(input_file_path), 'r')

    (target, total_pizzas) = input_file.readline().strip().split(' ')
    slice_arr = input_file.readline().strip().split(' ')

    return (int(target), int(total_pizzas), slice_arr)
    
def write_output_file(idx_array, input_file_path):
    Path("outputs").mkdir(parents=True, exist_ok=True)
    output_file = open('outputs/' + str(input_file_path[:-3]) + '.out', 'w+')

    output_file.write(str(len(idx_array)))
    output_file.write('\n')
    for id in idx_array:
        output_file.write(str(id) + ' ')

    output_file.close()
