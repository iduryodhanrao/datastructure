from itertools import combinations
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    comb = combinations(list(range(1,n+1)), k)
    result = []
    for i in list(comb):
        result.append(list(i))
        
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    n = 4
    k = 2
    print(find_combinations(n, k))  # Expected output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    # Test case 2
    n = 5
    k = 3
    print(find_combinations(n, k))  # Expected output: [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

    # Test case with n < k
    n = 3
    k = 5
    print(find_combinations(n, k))  # Expected output: [] (no combinations possible)