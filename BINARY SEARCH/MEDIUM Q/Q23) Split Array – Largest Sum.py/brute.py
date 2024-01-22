# METHOD- ( SAME QUESTION AS Q22 )

# The extremely naive approach is to check all possible answers from max(arr[]) to sum(arr[]). The minimum value for which we can make k subarrays will be our answer.
    
# STEPS-

# 1) First, we will find the maximum element and the summation of the given array.

# 2) We will use a loop(say maxSum) to check all possible answers from max(arr[]) to sum(arr[]).

# 3) Next, inside the loop, we will send ‘maxSum’, to the function countPartitions() function to get the number of partitions.

#         A) The first value of ‘maxSum’, for which the number of partitions will be equal to ‘k’, will be our answer. So, we will return that particular value of ‘maxSum’.

# 4) Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.  


# CODE-

def countPartitions(a, maxSum):
    n = len(a)  # size of array
    partitions = 1
    subarraySum = 0
    for i in range(n):
        if subarraySum + a[i] <= maxSum:
            # insert element to current subarray
            subarraySum += a[i]
        else:
            # insert element to next subarray
            partitions += 1
            subarraySum = a[i]
    return partitions

def largestSubarraySumMinimized(a, k):
    low = max(a)
    high = sum(a)

    for maxSum in range(low, high+1):
        if countPartitions(a, maxSum) == k:
            return maxSum
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)


# Output: The answer is: 60

# Complexity Analysis--

# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible values of time. Inside the loop, we are calling the countPartitions() function for each number. Now, inside the countPartitions() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.