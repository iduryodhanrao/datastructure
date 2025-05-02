#memeorization with recursion
def fibonacci_memo(n, memo):
    if n in memo: # 2. Check the memo
        return memo[n]
    if n <= 1:
        return n # Base case: F(0) = 0, F(1) = 1
    
    # 3. Store the result
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def find_fibonacci(n):
    memo = {} # 1. Create a memo (cache)
    return fibonacci_memo(n, memo)

# Example usage
#print(find_fibonnaci(10)) # Output: 55

# Test cases
if __name__ == "__main__":
    # Test case 1
    n = 10
    print(find_fibonacci(n))  # Expected output: 55 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55)
    
    # Test case 2
    n = 20
    print(find_fibonacci(n))  # Expected output: 6765 (Fibonacci sequence: ... , 4181, 6765)
    
    # Test case with n = 0
    n = 0
    print(find_fibonacci(n))  # Expected output: 0 (Fibonacci sequence: [0])
    
    # Test case with n = 1
    n = 1
    print(find_fibonacci(n))  # Expected output: 1 (Fibonacci sequence: [0, 1])