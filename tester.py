def test_solution(target, total_pizzas, slice_arr, idx_arr):
    slices = 0
    for id in idx_arr:
        slices += int(slice_arr[id])
    if (target - slices >= 0):
        print("Slice Delta: " + str(target - slices))
    else:
        print("Too Many Slices!")
    if (len(idx_arr) <= total_pizzas):
        print("Pizzas Ordered: " + str(len(idx_arr)))
    else:
        print("Too Many Pizzas")

