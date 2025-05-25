# Space complexity: O(1)
# Time complexity: O(n)
def sum_numbers(n):
    x = 0
    for i in range(1, n + 1):
        x += i
    print(x)

#more efficient
# Space complexity: O(1)
# Time complexity: O(1)
# 1 + 2+ 3 + ... n = n*(n+1)/2
# to avoid overflow when huge number .. divide first and then multiply

def findsum(n):
    x=n * ((n+1)/2)
    print(x)

if __name__ == "__main__":
    sum_numbers(3)
    findsum(3)


#similarly for sum of squares
# natural numbers: 1^2 + 2^2 + 3^2 + ... n^2 = n(n+1)(2n+1)/6
# even numbers : 2^2 + 4^2 + .....n^2 = 2n(n+1)(2n+1)/3
# odd numbers : 1^2 + 3^2 + .....n^2 = n(2n+1)(2n-1)/3