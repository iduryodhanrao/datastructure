
#time complexity - O(n)
#aux space complexity - O(n)
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

#time complexity - O(n)
#aux space complexity - O(1)
def facti(n):
    f=1
    for i in range(2,n+1):
        f=i*f
    return f

#time complexity - O(n)
#aux space complexity - O(1)
#nPr = n!/(n-r)!
def npr(n,r):
    return facti(n)/facti(n-r)

#time complexity - O(n)
#aux space complexity - O(1)
#nCr = n!/r!(n-r)!
def ncr(n,r):
    return facti(n)/(facti(n-r)*(facti(r)))
    
print(fact(3))
print(facti(5))
print(npr(6,3))
print(ncr(5,2))
