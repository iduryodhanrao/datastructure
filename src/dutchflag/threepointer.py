#Approach 1: Three pointers left and right and i

def swap(balls, i, j):
    tmp = balls[i]
    balls[i] = balls[j]
    balls[j] = tmp


def dutch_flag_sort(balls):
    left = 0
    right = len(balls) - 1
    i = 0
    
    while i <= right:
        if balls[i] == "R":
            swap(balls, i, left)
            left += 1
            i += 1
        elif balls[i] == "B":
            swap(balls, i, right)
            right -= 1
        else:
            i += 1
    
    return balls

# Test cases
if __name__ == "__main__":
    # Test case 1
    balls = ["G", "R", "B", "G", "R", "B"]
    print(dutch_flag_sort(balls))  # Expected output: ['R', 'R', 'G', 'G', 'B', 'B']

    # Test case 2
    balls = ["B", "G", "R", "G", "B", "R"]
    print(dutch_flag_sort(balls))  # Expected output: ['R', 'R', 'G', 'G', 'B', 'B']

    # Test case 3
    balls = ["G", "G", "G"]
    print(dutch_flag_sort(balls))  # Expected output: ['G', 'G', 'G']

    # Test case 4
    balls = ["R", "R", "R"]
    print(dutch_flag_sort(balls))  # Expected output: ['R', 'R', 'R']

    # Test case 5
    balls = ["B", "B", "B"]
    print(dutch_flag_sort(balls))  # Expected output: ['B', 'B', 'B']
