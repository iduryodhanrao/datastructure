"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n ^ 2).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range (0, n - 1):
        # Move arr[i + 1] to its correct position.
        j = i + 1
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    return arr;
