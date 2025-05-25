# Time complexity: O(1)
# Space complexity: O(1)
def swap2numbers(m,n):
    x=m
    m=n
    n=x
    return(m,n)

# without using the 3rd variable
def swap_bytuple(m,n):
    m,n=n,m
    return(m,n)

if __name__ == "__main__":
    print(swap2numbers(5,6))
    print(swap_bytuple(5,6))