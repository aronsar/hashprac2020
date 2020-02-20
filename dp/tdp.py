import numpy as np

def dp(slice_arr, target):
    slice_arr = [int(x) for x in slice_arr]
    target = int(target)
    max_slices = np.empty([len(slice_arr)+1, target+1])
    use_pizza = np.empty([len(slice_arr)+1, target+1])

    for i in range(len(slice_arr)+1):
        for n in range(target+1):
            if i == 0 or n == 0:
                max_slices[i, n] = 0
                use_pizza[i, n] = 0
            else:
                p = slice_arr[i-1]
                if p > n: # max_slices in this pizza more than total needed max_slices
                    max_slices[i, n] = max_slices[i-1, n]
                    use_pizza[i, n] = 0
                else:
                    if max_slices[i-1, n-p] + p > max_slices[i-1, n]:
                        max_slices[i, n] = max_slices[i-1, n-p] + p
                        use_pizza[i, n] = 1
                    else:
                        max_slices[i, n] = max_slices[i-1, n]
                        use_pizza[i, n] = 0
    
    n = target
    idx_arr = []
    for i in range(len(slice_arr),0,-1):
        if use_pizza[i, n] == 1:
            n -= slice_arr[i-1]
            idx_arr.append(i-1)
    print(idx_arr[::-1])    
    return idx_arr[::-1]
