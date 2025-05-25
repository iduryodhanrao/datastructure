#Time complexity: O(1)
#Space complexity: O(1)
def multiplication_table(n):
    #return [f"{n}*{i}={ n*i }" for i in range(1, 11)]
    for i in range(1, 11):
        print (f"{n} * {i} = {n * i}")

#recursive function to print multiplication table
def multiplication_table_recursive(n, i=1):
    if i == 11:
        return
    print(f"{n} * {i} = {n * i}")
    multiplication_table_recursive(n, i + 1)

if __name__ == "__main__":
    multiplication_table(5)
    multiplication_table_recursive(6)
    