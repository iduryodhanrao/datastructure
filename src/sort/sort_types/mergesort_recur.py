"""
Asymptotic complexity in terms of size of `arr` `n`:
* Time: O(n * log(n)).
* Auxiliary space: O(n).
* Total space: O(n).
"""

def msort(arr, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    msort(arr, start, mid)
    msort(arr, mid + 1, end)
    i = start
    j = mid + 1
    mlist = []
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            mlist.append(arr[i])
            i += 1
        elif arr[j] < arr[i]:
            mlist.append(arr[j])
            j += 1
    while i <= mid:
        mlist.append(arr[i])
        i += 1
    while j <= end:
        mlist.append(arr[j])
        j += 1
    arr[start:end + 1] = mlist

def merge_sort(arr):
    msort(arr, 0, len(arr) - 1)
    return arr
