import numpy as np
cimport numpy as np
cimport cython

NP_INT = np.int32
ctypedef np.int32_t NP_INT_t

cpdef dp(int[:] slice_arr, int target):
    cdef int num_pizzas = len(slice_arr)
    cdef int target_slices = target

    cdef NP_INT_t[:,:] max_slices = np.zeros([num_pizzas+1, target_slices+1], dtype=NP_INT)
    cdef NP_INT_t[:,:] use_pizza = np.zeros([num_pizzas+1, target_slices+1], dtype=NP_INT)
    
    cdef int p

    for i in range(num_pizzas+1):
        for n in range(target_slices+1):
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

