"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n^2).
* Auxiliary space: O(1).
* Total space: O(n).
"""

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  # Store the value to be inserted
        j = i - 1

        # Shift elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the stored value at the correct position
        arr[j + 1] = key

    return arr
