#Approach 1: Sort and Use sorted 2 sum

def find_zero_sum(A):
    A.sort()
    n = len(A)
    result = []
    
    i = 0
    
    while i < n - 2 and A[i] <= 0:
        j = i + 1
        k = n - 1
        
        while j < k:
            triplet_sum = A[i] + A[j] + A[k]
            if triplet_sum > 0:
                k -= 1
            elif triplet_sum < 0:
                j += 1
            else:
                result.append("{},{},{}".format(A[i], A[j], A[k]))
                j += 1
                k -= 1
                
                # Skip over all duplicate A[j]'s 
                while A[j] == A[j-1] and j < k:
                    j += 1
                
                # Skip over all duplicate A[k]'s
                while A[k] == A[k+1] and j < k:
                    k -= 1
                    
        i += 1
        
        while A[i] == A[i-1] and i < n - 2:
            i += 1
            
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    A = [-1, 0, 1, 2, -1, -4]
    print(find_zero_sum(A))  # Expected output: [[-1, -1, 2], [-1, 0, 1]]
    
    # Test case 2
    A = [0, 0, 0]
    print(find_zero_sum(A))  # Expected output: [[0, 0, 0]]
    
    # Test case with no zero-sum triplet
    A = [1, 2, 3]
    print(find_zero_sum(A))  # Expected output: []