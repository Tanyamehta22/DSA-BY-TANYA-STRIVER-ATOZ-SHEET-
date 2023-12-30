# METHOD--
# A simple solution is consider every subarray and count 1’s in every subarray. Finally return size of largest subarray with all 1’s. An efficient solution is traverse array from left to right. If we see a 1, we increment count and compare it with maximum so far. If we see a 0, we reset count as 0.

# CODE-

# Returns count of maximum 
# consecutive 1's in binary
# array arr[0..n-1]
def getMaxLength(arr,n):

    # initialize count
    count=0

    # initialize max
    result=0

    for i in range(0,n):

        # Reset count when 0 is found
        if (arr[i]==0):
            count = 0

         # If 1 is found, increment count
        # and update result if count 
        # becomes more.
        else:

            # increase count    
            count +=1
            result = max(result,count)

    return result

#  Driver code--
arr = [1, 1, 0, 0, 1, 0, 1, 
             0, 1, 1, 1, 1] 
n = len(arr) 
 
print(getMaxLength(arr, n))



# Output
# 4


# Time Complexity : O(n) 
# Auxiliary Space : O(1)



