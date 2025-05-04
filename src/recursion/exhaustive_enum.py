def binstring(a,n):
    if n == 0:
        print(a)    
    else:
        binstring(a+"0",n-1)
        binstring(a+"1",n-1)
#binstring("",4)

def binstring2(n):
    if n == 1:
        return ["0", "1"]
    else:
        prev = binstring2(n-1)
        result=[]
        for s in prev:
            result.append(s + "0")
            result.append(s + "1")
        return result
print(binstring2(4))