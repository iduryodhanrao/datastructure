"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""

def merge(arr, left, mid, right):
    l = arr[left:mid+1]  # copies the integers to list l from arr
    r = arr[mid+1:right+1]  # copies the integers to list r from arr
    i = 0
    j = 0
    k = left
    # merges lists l and r back into arr
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    # merges remaining elements of lists l and r
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

def split(arr, l, h):
    # divide the list into blocks of size [1, 2, 4, 8, ..]
    blocks = 1
    while blocks <= h - l:
        i = l
        while i < h:
            left = i
            mid = min(i + blocks - 1, h)
            right = min(i + 2 * blocks - 1, h)
            merge(arr, left, mid, right)
            i += 2 * blocks
        blocks *= 2

def merge_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    split(arr, left, right)
    return arr
