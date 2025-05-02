
def insertion_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        #print(key)
        for j in range(i-1,-1,-1):
            if key < arr[j]:
                #print(j, arr[j])
                arr[j+1] = arr[j]
                j=j-1
            else:
                break
        arr[j+1] = key
        #print (arr)
    '''
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr) '''
    return arr
