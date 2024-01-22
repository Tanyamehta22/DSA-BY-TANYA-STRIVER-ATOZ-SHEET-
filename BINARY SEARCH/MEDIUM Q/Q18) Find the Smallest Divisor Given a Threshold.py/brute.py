# METHOD-

# The extremely naive approach is to check all possible divisors from 1 to max(arr[]). The minimum number for which the result <= threshold value, will be our answer.
    
# STEPS-

# 1) We will run a loop(say d) from 1 to max(arr[]) to check all possible divisors.

# 2) To calculate the result, we will iterate over the given array using a loop. Within this loop, we will divide each element in the array by the current divisor, d, and sum up the obtained ceiling values.

# 3) Inside the outer loop, If result <= threshold: We will return d as our answer.

# 4) Finally, if we are outside the nested loops, we will return -1.

# CODE-

import math

def smallestDivisor(arr, limit):
    n = len(arr)  # size of array
    maxi = max(arr)
    # Find the smallest divisor
    for d in range(1, maxi+1):
        # Find the summation result
        sum = 0
        for i in range(n):
            sum += math.ceil(arr[i] / d)
        if sum <= limit:
            return d
    return -1

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)




# Output:The minimum divisor is: 3

# Complexity Analysis--

# Time Complexity: O(max(arr[])*N), where max(arr[]) = maximum element in the array, N = size of the array.
# Reason: We are using nested loops. The outer loop runs from 1 to max(arr[]) and the inner loop runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.
