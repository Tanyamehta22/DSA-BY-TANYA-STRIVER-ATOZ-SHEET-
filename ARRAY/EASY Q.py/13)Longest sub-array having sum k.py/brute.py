# METHOD-
# Consider the sum of all the sub-arrays and return the length of the longest sub-array having the sum ‘k’. Time Complexity is of O(n^2).

# CODE--

# function to find the length of longest
# subarray having sum k
def lenOfLongSubarr(arr, N, K):
   
    # Variable to store the answer
    maxlength = 0
    for i in range(0,N):
        # Variable to store sum of subarrays
        Sum=0

        for j in range(i,N):

            # Storing sum of subarrays
            sum+=arr[j]

            # if Sum equals K
            if (sum==K):

                # Update maxLength
                maxlength = max(maxlength, j-i+1)

    # Return the maximum length            
    return maxlength

# Driver Code
# Given input
arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15
 
# Function Call
print("Length = " , lenOfLongSubarr(arr, n, k))



# Output-
# Length = 4


# Time Complexity: O(N2), for calculating the sum of all subarrays.
# Auxiliary Space: O(1), as constant extra space is required.