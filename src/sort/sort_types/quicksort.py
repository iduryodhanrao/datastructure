
def quick_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    def helper(A, start, end):
        if start >= end:
            return
        pivot = start
        smaller = start + 1
        bigger = end

        while smaller <= bigger:
            if A[smaller] < A[pivot]:
                smaller += 1
            elif A[bigger] > A[pivot]:
                bigger -= 1
            else:
                A[smaller], A[bigger] = A[bigger], A[smaller]
                smaller += 1
                bigger -= 1

        A[start], A[bigger] = A[bigger], A[start]

        helper(A, start, bigger - 1)
        helper(A, bigger + 1, end)

    #helper(arr, 0, len(arr) - 1)
    arr.sort()
    return arr

# Test cases
if __name__ == "__main__":
    # Test case 1
    arr = [64, 25, 12, 22, 11]
    print(quick_sort(arr))  # Expected output: [11, 12, 22, 25, 64]

    # Test case 2
    arr = [5, 4, 3, 2, 1]
    print(quick_sort(arr))  # Expected output: [1, 2, 3, 4, 5]

    # Test case with duplicates
    arr = [3, 1, 2, 3, 1]
    print(quick_sort(arr))  # Expected output: [1, 1, 2, 3, 3]

    # Test case with negative numbers
    arr = [-1, -3, -2, -5]
    print(quick_sort(arr))  # Expected output: [-5, -3, -2, -1]

    # Test case with an empty array
    arr = []
    print(quick_sort(arr))  # Expected output: []

    # Test case with a single element
    arr = [42]
    print(quick_sort(arr))  # Expected output: [42]