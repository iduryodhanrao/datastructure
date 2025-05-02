
def find_fibonacci(n):
    """
    Args:
     n(int32)
    Returns:
     int32
    """
    # Write your code here.
    '''if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return find_fibonacci(n-1) + find_fibonacci(n-2)
        
    '''
    i=2
    a=f=0
    b=1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        while i<=n:
            f=a+b
            a=b
            b=f
            i= i+ 1
        return f

# Test cases
if __name__ == "__main__":
    # Test case 1
    n = 5
    print(find_fibonacci(n))  # Expected output: 3 (Fibonacci sequence: 0, 1, 1, 2, 3, 5)
    
    # Test case 2
    n = 10
    print(find_fibonacci(n))  # Expected output: 34 (Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
    
    # Test case with n = 0
    n = 0
    print(find_fibonacci(n))  # Expected output: 0 (Fibonacci sequence: [0])
    
    # Test case with n = -1 (invalid input)
    n = -1
    print(find_fibonacci(n))  # Expected output: None or an error message (invalid input)