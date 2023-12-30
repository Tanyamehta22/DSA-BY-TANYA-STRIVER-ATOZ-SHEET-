# METHOD--(USING SLIDING WINDOW)
# This approach won’t work for negative numbers

# STEPS--
# In the variable-size sliding window, we do three things.

# 1. calculation, in this case doing the sum.

# 2. drawing results out of calculations. in this case, extracting the size of the window if the sum reaches K (target).

# 3. adjusting the window. in this case, increasing the size of the window if the sum is less than K(target) or decreasing the size if the sum is greater than K(target).

# The approach is to use the concept of the variable-size sliding window using 2 pointers
# Initialize i, j, and sum = 0. If the sum is less than k just increment j, if the sum is equal to k compute the max and if the sum is greater than k subtract the ith element while the sum is greater than k.


# CODE--

# function to find the length of longest
# subarray having sum k
import sys

def lenOfLongSubarr(A,N,K):
    i,j, sum= 0,0,0
    maxLen= -sys.maxsize-1

    while(j<N):
        sum+=A[j]
        if(sum<K):
            j+=1
        elif(sum==K):
            maxLen=max(maxLen,j-i+1)
            j+=1
        elif(sum>K):
            while(sum>K):
                sum-=A[i]
                i+=1  
            if(sum==K):
                maxLen=max(maxLen,j-i+1)
            j+=1
    return maxLen    

# Driver Code
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15
print("Length = "+ str(lenOfLongSubarr(arr, n, k)))        



# Output--
# Length = 4


# Time Complexity: O(N), where N is the length of the given array.
# Auxiliary Space: O(1), as constant extra space is required.
