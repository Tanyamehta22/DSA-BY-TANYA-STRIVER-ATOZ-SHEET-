# METHOD--(HASHING)

# STEP--

# 1) Initialize sum = 0 and maxLen = 0.

# 2) Create a hash table having (sum, index) tuples.

# 3) For i = 0 to n-1, perform the following steps:
#   A)Accumulate arr[i] to sum.

#   B)If sum == k, update maxLen = i+1.

#   C)Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.  

#   D)Check if (sum-k) is present in the hash table or not. If present, then obtain index of (sum-k) from the hash table as index. Now check if maxLen < (i-index), then update maxLen = (i-index).

# 4) Return maxLen.

# CODE--

# function to find the longest
# subarray having sum k
def lenOfLongSubarr(arr,n,K):

    # dictionary mydict implemented
    # as hash map
    mydict=dict()

    
    #Initialize sum and maxLen with 0
    sum=0
    maxlength=0

    # traverse the given array
    for i in range(n):

        
        # accumulate the sum
        sum+=arr[i]

        # when subArray starts from index '0'
        if(sum==K):
            maxlength= i+1

        # check if 'sum-k' is present in
        # mydict or not
        elif (sum-K) in mydict:
            maxlength=max(maxlength,i-mydict[sum-K])

         # if sum is not present in dictionary
        # push it in the dictionary with its index
        if sum not in mydict:
            mydict[sum] = i  

    return maxlength  

# Driver Code
if __name__ == '__main__':
    arr = [10, 5, 2, 7, 1, 9]
    n = len(arr)
    k = 15
    print("Length =", lenOfLongSubarr(arr, n, k))      

# Output--
# Length = 4

# Time Complexity: O(N), where N is the length of the given array.
# Auxiliary Space: O(N), for storing the maxLength in the HashMap.        


# NOTE(IMP)--- THIS APPROACH IS OPTIMAL FOR NEGATIVE NO. INSUBARRAY     
