# METHOD--

# The idea is to use the Kadane’s Algorithm.

# STEPS--

# 1) Initialize currMax and globalMax to first value of the input array. Initialize endIndex, startIndex, globalMaxStartIndex to 0.  ( endIndex, startIndex store the start and end indices of the max sum sub-array ending at i. globalMaxStartIndex stores the startIndex of the globalMax )

# 2) For each element in the array starting from index (say i) 1, update currMax and startIndex to i if nums[i] > nums[i] + currMax. Else only update currMax.

# 3) Update globalMax if currMax>globalMax. Also update globalMaxStartIndex.

# 4) Now print the subarray between [start index, globalMaxStartIndex].

# CODE--

# Function to print the elements
# of Subarray with maximum sum

def SubarrayWithMaxSum(nums):

    # Initialize currMax and globalMax
    # with first value of nums
    currMax = nums[0]
    globalMax = nums[0]

    # Initialize endIndex startIndex,globalStartIndex
    endIndex = 0
    startIndex=0
    globalMaxStartIndex=0


    # Iterate for all the elements of the array
    for i in range(1,len(nums)):

        # Update currMax and startIndex
        if (nums[i]>nums[i] + currMax):
            currMax = nums[i]
             # update the new startIndex
            startIndex = i

        # Update currMax
        elif (nums[i]<nums[i]+ currMax):
            currMax+=nums[i] 

        # Update globalMax and globalMaxStartIndex
        if (currMax>globalMax):
            globalMax=currMax
            endIndex=i
            globalMaxStartIndex= startIndex 

    # Printing the elements of subarray with max sum
    for i in range(globalMaxStartIndex, endIndex + 1):
        print(nums[i], end=' ')              


# Driver code
if __name__ == '__main__':
 
    # Given array arr[]
    arr = []
    arr.append(-2)
    arr.append(-5)
    arr.append(6)
    arr.append(-2)
    arr.append(-3)
    arr.append(1)
    arr.append(5)
    arr.append(-6)
    # Function call
    SubarrayWithMaxSum(arr)


# Output-
# 6 -2 -3 1 5

# Time complexity: O(N) 

# Auxiliary Space: O(1)    

