#Time complexity: O(1)
#Space complexity: O(1)

#using modulus operator to check if a number is even or odd
def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

#using bitwise operator to check if a number is even or odd
#example -- 11 & 1 = 1, which is not equal to 0, hence odd
def is_even_bitwise(n):
    return n & 1 == 0

#using bitwise shift operator to check if a number is even or odd
#example -- 11 >> 1 = 5, 5 << 1 = 10, which is not equal to 11, hence odd 
def is_even_shift(n):
    return (n >> 1) << 1 == n


if __name__ == "__main__":
    # Test cases for is_even function
    test_number = 5
    print(f"{test_number} is even: {is_even(test_number)}")
    print(f"{test_number} is even: {is_even_bitwise(test_number)}")
    print(f"{test_number} is even: {is_even_shift(test_number)}")