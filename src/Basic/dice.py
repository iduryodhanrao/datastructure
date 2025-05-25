# Opposite face of the dice give one side
# Time complexity: O(1)
# Space complexity: O(1)
def dice(n: int):
    if n in range(1,7):
        oppface = 7-n
        print(oppface)
    else:
        print("enter between 1 to 6")

if __name__ == "__main__":
    dice(2)
    dice(6)
