#Approach 2: Use unsorted 2 sum with map/set

def find_zero_sum(A):
   n = len(A)
   result_set = set()
  
   i = 0
  
   while i < n - 2:
       j = i + 1
       k = n - 1
      
       target = -A[i]
       tracking_set = set()
       for j in range(i+1, n):
           if target - A[j] in tracking_set:
               first, second, third = sorted([A[i], A[j], target - A[j]])
               result_set.add("{},{},{}".format(first, second, third))
           tracking_set.add(A[j])
                  
       i += 1
          
   return list(result_set)

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