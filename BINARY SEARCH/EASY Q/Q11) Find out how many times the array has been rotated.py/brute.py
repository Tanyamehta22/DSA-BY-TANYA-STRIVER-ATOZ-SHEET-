# METHOD--

# 1) We can easily observe that the number of rotations in an array is equal to the index(0-based index) of its minimum element.

# 2) So, in order to solve this problem, we have to find the index of the minimum element.( I.E QUESTION-10 )

# STEPS--

# 1) First, we will declare an ‘ans’ and an ‘index’ variable initialized with a large number and -1 respectively.

# 2) Next, we will iterate through the array and compare each element with the variable called ‘ans’. Whenever we encounter an element ‘arr[i]’ that is smaller than ‘ans’, we will update ‘ans’ with the value of ‘arr[i]’ and also update the ‘index’ variable with the corresponding index value, ‘i’.

# 3) Finally, we will return ‘index’ as our answer.

# CODE-

# Returns count of rotations for 
# an array which is first sorted 
# in ascending order, then rotated 
def countRotations(arr, n): 
  
    # We basically find index 
    # of minimum element 
    min = arr[0] 
    min_index = 0
    for i in range(0, n): 
      
        if (min > arr[i]): 
          
            min = arr[i] 
            min_index = i 
          
    return min_index; 
  
  
# Driver code 
arr = [15, 18, 2, 3, 6, 12] 
n = len(arr) 
print(countRotations(arr, n)) 


 
# Output--
# 2

# Time Complexity: O(N) 
# Auxiliary Space: O(1) 