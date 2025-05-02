#Approach 1: Create a single even partition to the left of left pointer

def swap(numbers, i, j):
    tmp = numbers[i]
    numbers[i] = numbers[j]
    numbers[j] = tmp

def segregate_evens_and_odds(numbers):
    left = 0
    i = 0
    
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            swap(numbers, left, i)
            left += 1
        i += 1
    
    return numbers
