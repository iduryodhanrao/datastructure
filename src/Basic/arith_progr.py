#Arithmatic progression - x = a + (n-1)*d
# Time complexity: O(1)
# Auxilary Space complexity: O(1)
def ap(a1,a2,n):
    d = a2-a1
    x = a1 + (n-1)*d
    print(x)

if __name__=="__main__":
    ap(2,3,4)
    ap(1,3,10)