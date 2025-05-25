#sqrt (n) -- avoids unnecessary traversal till nth value. 
#Time Complexity: O(√n)
#Auxiliary Space: O(1)
import math
def isprime(n):
    if n in [0,1]:
        return False
    #x = int(n/2)
    x = int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i == 0:
            return False
    return True
if __name__ =="__main__":
    print(isprime(11))
    print(isprime(15))
    print(isprime(1))
    s="12234"
    print(int(s[-2:]))