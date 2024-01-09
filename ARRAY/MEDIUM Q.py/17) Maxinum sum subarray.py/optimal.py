# METHOD-(USING Kadane’s Algorithm)

# The idea of Kadane’s algorithm is to maintain a variable max_ending_here that stores the maximum sum contiguous subarray ending at current index and a variable max_so_far stores the maximum sum of contiguous subarray found so far, Everytime there is a positive-sum value in max_ending_here compare it with max_so_far and update max_so_far if it is greater than max_so_far.

# So the main Intuition behind Kadane’s Algorithm is, 

# 1) The subarray with negative sum is discarded (by assigning max_ending_here = 0 in code).

# 2) We carry subarray till it gives positive sum.


# STEPS--

# 1) Initialize the variables max_so_far = INT_MIN and max_ending_here = 0

# 2) Run a for loop from 0 to N-1 and for each index i: 

#        A) Add the arr[i] to max_ending_here.

#        B) If  max_so_far is less than max_ending_here then update max_so_far  to max_ending_here.

#        C) If max_ending_here < 0 then update max_ending_here = 0

# 3) Return max_so_far

# CODE-
# Function to find the maximum contiguous subarray
from sys import maxint

def maxSubArraySum(a,size):
    max_so_far = -maxint-1
    max_ending_here=0

    for i in range(0,size):
        max_ending_here=max_ending_here+a[i]

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here<0:
            max_ending_here=0
    return max_so_far  


# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
 
print ( maxSubArraySum(a, len(a)))
           

# Output--
# Maximum contiguous sum is 7

# Time Complexity: O(N)

# Auxiliary Space: O(1)
