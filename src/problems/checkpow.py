"""Input:  x = 10, y = 1000
Output: True
explaination x^3 = 10^3 = 1000

Input:  x = 10, y = 1001
Output: False
"""

import math

#Iterative
#Time complexity: O(Logxy)
#Auxiliary space: O(1)
def ispoweri(x,y):
    if x == 1:
        return y == 1
    pow=1
    while pow < y:
        pow = x*pow
        if pow == y:
            return True
    return False

    

#Time complexity: O(1)
#Auxiliary space: O(1)
def ispower(x,y):
    res = math.log(y)/math.log(x)
    #log 1000 / log 10 = log10(1000) = 3
    #log y/ log x = log [base x] y 
    return res == math.floor(res)



print(ispower(2,128))
print (ispoweri(10,1000))