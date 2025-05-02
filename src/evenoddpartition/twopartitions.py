#Approach 2: Create two partitions for evens and odds
def swap(numbers, i, j):
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp

def segregate_evens_and_odds(numbers):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        if numbers[left] % 2 == 0:
            left += 1
        elif numbers[right] % 2 == 1:
            right -= 1
        else:
            #A[left] is odd A[right] is even
            swap(numbers, left, right)
            left += 1
            right -= 1
    return numbers
