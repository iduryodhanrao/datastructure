
"""
Asymptotic complexity in terms of `n` and 'k':
* Time: O(2^n * k).
* Auxiliary space: O(n).
* Total space: O(nCk * k).
"""

def combinations_recursive(current_number, n, k, current, result):
    if len(current) == k:
        result.append(list(current))
        return
    if current_number == n + 1:
        return

    current.append(current_number)
    combinations_recursive(current_number + 1, n, k, current, result)
    current.pop()
    combinations_recursive(current_number + 1, n, k, current, result)

def find_combinations(n, k):
    result = []
    current = []

    combinations_recursive(1, n, k, current, result)
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