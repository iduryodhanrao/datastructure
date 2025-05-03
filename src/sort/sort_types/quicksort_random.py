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
# quick_sort([3, 6, 8, 10, 1, 2, 1])

# test cases

if __name__ == "__main__":
    import random
    arr = [random.randint(0, 100) for _ in range(10)]
    print("Unsorted array:", arr)
    sorted_arr = quick_sort(arr)
    print("Sorted array:", sorted_arr)
    assert sorted_arr == sorted(arr), "The quick_sort function did not sort the array correctly."