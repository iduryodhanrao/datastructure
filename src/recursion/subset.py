
def count_all_subsets(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    if n==0:
        return 1
    else:
        return 2*count_all_subsets(n-1)
    return 0

# Test cases
if __name__ == "__main__":
    # Test case 1
    n = 3
    print(count_all_subsets(n))  # Expected output: 8 (subsets: [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3])
    
    # Test case 2
    n = 0
    print(count_all_subsets(n))  # Expected output: 1 (only the empty set)
    
    # Test case with negative n (invalid input)
    n = -1
    print(count_all_subsets(n))  # Expected output: 0 (no subsets possible)