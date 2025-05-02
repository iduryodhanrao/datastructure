'''
"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n ^ 2).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def bubble_sort(arr):
    for start in range(len(arr)):
        for i in range(len(arr)-1, start, -1):
            if arr[i - 1] > arr[i]:
                (arr[i - 1], arr[i]) = (arr[i], arr[i - 1])

    return arr
    '''
def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr