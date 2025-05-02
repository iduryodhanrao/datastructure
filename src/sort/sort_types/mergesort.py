
def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n=len(arr)
    if n<=1:
        return arr
    mid = n // 2
    #print(mid)
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    sorted_left=merge_sort(left_arr)
    sorted_right=merge_sort(right_arr)
    return merge(sorted_left,sorted_right)
    
def merge(left,right):
    l=len(left)
    r=len(right)
    i=j=0
    resultset=[]
    while i<l and j<r:
        if left[i] <= right[j]:
            resultset.append(left[i])
            i+=1
        else:
            resultset.append(right[j])
            j+=1
    while i<l:
        resultset.append(left[i])
        i+=1
    while j<r:
        resultset.append(right[j])
        j+=1
        
    #print(resultset)
    return resultset

# Test cases
if __name__ == "__main__":
    # Test case 1
    arr = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr))  # Expected output: [3, 9, 10, 27, 38, 43, 82]

    # Test case 2
    arr = [5, 2, 9, 1, 5, 6]
    print(merge_sort(arr))  # Expected output: [1, 2, 5, 5, 6, 9]

    # Test case with an already sorted array
    arr = [1, 2, 3, 4, 5]
    print(merge_sort(arr))  # Expected output: [1, 2, 3, 4, 5]

    # Test case with an empty array
    arr = []
    print(merge_sort(arr))  # Expected output: []

    # Test case with a single element array
    arr = [42]
    print(merge_sort(arr))  # Expected output: [42]