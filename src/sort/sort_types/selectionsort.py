
'''"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n ^ 2).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def selection_sort(arr):
    for i in range(len(arr)):
        # Find the ith smallest element and swap it with arr[i]
        min = i
        for inner in range(i, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
        (arr[i],arr[min]) = (arr[min],arr[i])

    return arr
'''

def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        # Find the ith smallest element and swap it with arr[i]
        min = i
        for inner in range(i+1, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
        (arr[i],arr[min]) = (arr[min],arr[i])
        #print(arr)

    return arr

# Test cases
if __name__ == "__main__":
    # Test case 1
    arr = [64, 25, 12, 22, 11]
    print(selection_sort(arr))  # Expected output: [11, 12, 22, 25, 64]

    # Test case 2
    arr = [5, 4, 3, 2, 1]
    print(selection_sort(arr))  # Expected output: [1, 2, 3, 4, 5]

    # Test case with duplicates
    arr = [3, 1, 2, 3, 1]
    print(selection_sort(arr))  # Expected output: [1, 1, 2, 3, 3]

    # Test case with negative numbers
    arr = [-1, -3, -2, -5]
    print(selection_sort(arr))  # Expected output: [-5, -3, -2, -1]

    # Test case with an empty array
    arr = []
    print(selection_sort(arr))  # Expected output: []

    # Test case with a single element
    arr = [42]
    print(selection_sort(arr))  # Expected output: [42]