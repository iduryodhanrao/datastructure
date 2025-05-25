
# Time complexity: O(1)
# Space complexity: O(1)
#find closed divisor number 
#using remainder 
def closest(n,m):
    rem = n%m
    if rem >= m/2:
        y = n + (m-rem)
    else:
        y = n + rem
    print(y)

#using quotient 
def closest1(n,m):
    quo = int(n/m)
    n1 = m*quo
    n2 = m*(quo+1)
    if abs(n - n1) <  abs(n - n2):
        print(n1)
    else:
        print(n2)

if __name__ == "__main__":
    closest1(13,4)
    closest1(15,6)