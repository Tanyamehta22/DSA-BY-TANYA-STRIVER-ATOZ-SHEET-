# METHOD-( USING BINARY SEARCH--- MIN(MAX) )

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Upon closer observation, we can recognize that our answer space, represented as [max(arr[]), sum(arr[])], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEPS-

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).

# 2) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Eliminate the halves based on the number of subarrays returned by countPartitions():
# We will pass the potential value of ‘maxSum’, represented by the variable ‘mid’, to the ‘countPartitions()‘ function. This function will return the number of partitions we can make.

#         A) If partitions > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

#         B) Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

# 4) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.

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
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        partitions = countPartitions(a, mid)
        if partitions > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

a = [10, 20, 30, 40]
k = 2
ans = largestSubarraySumMinimized(a, k)
print("The answer is:", ans)


# Output:The answer is: 60.

# Complexity Analysis--

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countPartitions() function for the value of ‘mid’. Now, inside the countPartitions() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

