"""
sum of digits, reverse numbers etc dealing with digits of number provided
Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21
"""
#Time Complexity: O(log10n), as we are iterating over all the digits.
#Auxiliary Space: O(1)
#iterative approach
def sumdigits(n):
    sum = 0
    while n > 0:
        x = n%10
        sum = sum + x
        n = int( n / 10)
    print(sum)
#recursion approach
#Time Complexity: O(log10n), as we are iterating over all the digits.
#Auxiliary Space: O(log10n) because of function call stack.
def sumdigits_recursion(n):
    if n == 0:
        return 0
    x = n%10
    n = int( n / 10)
    return x + sumdigits_recursion(n)

if __name__ =="__main__":
    sumdigits(687)
    print(sumdigits_recursion(687))