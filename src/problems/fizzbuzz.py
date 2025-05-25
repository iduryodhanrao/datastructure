"""Given an integer n, for every positive integer i <= n, the task is to print,

"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3,
"Buzz" if i is divisible by 5
"i" as a string, if none of the conditions are true.
Examples:

Input: n = 3
Output: ["1", "2", "Fizz"]

Input: n = 10
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
"""
#Time Complexity: O(n), since we need to traverse the numbers from 1 to n in any condition.
#Auxiliary Space: O(n), for storing the result
def fizzBuzz(n):
    res = []
    mp = {3: "Fizz", 5:"Buzz"}
    divisors = [3,5]
    for i in range(1,n+1):
        s = ""
        for d in divisors:
            if i%d == 0:
                s = s + mp[d]
        if not s:
            s = s + str(i)
        res.append(s)
    return res

print(fizzBuzz(20))
