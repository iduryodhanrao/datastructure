def dutch_flag_sort(balls):
    red_ptr = -1
    grn_ptr = -1

    for i in range(len(balls)):
        if balls[i] == 'G':
            grn_ptr += 1
            balls[grn_ptr], balls[i] = balls[i], balls[grn_ptr]
        elif balls[i] == 'R':
            grn_ptr += 1
            balls[grn_ptr], balls[i] = balls[i], balls[grn_ptr]
            red_ptr += 1
            balls[red_ptr], balls[grn_ptr] = balls[grn_ptr], balls[red_ptr]

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