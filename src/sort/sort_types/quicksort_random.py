"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""

def qsort(arr, start, end):
    if start >= end:
        return
    # Pick a random element as pivot.
    randindex = random.randint(start, end)
    arr[randindex], arr[start] = arr[start], arr[randindex]
    pivot = arr[start]
    smaller = start
    bigger = start
    for bigger in range(start + 1, end + 1):
        if arr[bigger] <= pivot:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
    # Place pivot in the right spot
    arr[start], arr[smaller] = arr[smaller], arr[start]
    qsort(arr, start, smaller - 1)
    qsort(arr, smaller + 1, end)

def quick_sort(arr):
    qsort(arr, 0, len(arr) - 1)
    return arr
