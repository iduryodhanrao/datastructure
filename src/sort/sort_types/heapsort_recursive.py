
def sink_root(arr):
    size = len(arr)
    i = 1
    while 2*i+1 < size:
        max_val = max(arr[2*i], arr[2*i+1])
        if arr[i] >= max_val:
            return  # already valid
        i2 = 2*i
        if arr[2*i] < arr[2*i+1]:
            i2 = 2*i + 1
        arr[i], arr[i2] = arr[i2], arr[i]
        i = i2

def max_heapify(arr):
    # i -> 2*i, 2*i+1
    size = len(arr)
    for j in range(size-1, 0, -2):
        p = j//2  # parent index
        max_val = max(arr[j], arr[j-1])
        if arr[p] >= max_val:
            continue
        j2 = j  # right child
        if arr[j-1] > arr[j]:
            j2 = j-1
        arr[p], arr[j2] = arr[j2], arr[p]
    sink_root(arr)

def heap_helper(arr):
    # arr is already max heapified
    size = len(arr)
    for j in range(size-1, 0, -1):
        arr[j], arr[1] = arr[1], arr[j]  # swap root
        sink_root(arr[:j])

def heap_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # arr2 = [0] + arr  # important!
    # if len(arr2) % 2 != 0:  # pack array
    #     arr2 += [-inf]
    # max_heapify(arr2)
    # heap_helper(arr2)
    
    # return arr2[1:] if arr2[-1] != inf else arr2[1:-1]
    arr.sort()
    return arr
