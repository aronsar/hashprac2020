from pathlib import Path


def load_input_file(input_file_path):
    with open("inputs/" + str(input_file_path), 'r') as input_file:
        data = input_file.read().splitlines()
    
    (target, total_pizzas) = map(int, data[0].split(" "))
    slice_arr = list(map(int, data[1].split(" ")))

    return int(target), int(total_pizzas), slice_arr


def write_output_file(idx_array, input_file_path):
    Path("outputs").mkdir(parents=True, exist_ok=True)
    with open('outputs/' + str(input_file_path[:-3]) + '.out', 'w+') as output_file:
        output_file.write(str(len(idx_array)))
        output_file.write('\n')
        for id in idx_array:
            output_file.write(str(id) + ' ')

        output_file.close()
