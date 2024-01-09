# METHOD--(PRESUM)

# An efficient solution is while traversing the array, storing sum so far in currsum. Also, maintain the count of different values of currsum in a map. If the value of currsum is equal to the desired sum at any instance increment count of subarrays by one. 

# The value of currsum exceeds the desired sum by currsum – sum. If this value is removed from currsum then the desired sum can be obtained. From the map, find the number of subarrays previously found having sum equal to currsum-sum. Excluding all those subarrays from the current subarray, gives new subarrays having the desired sum. 

# So increase count by the number of such subarrays. Note that when currsum is equal to the desired sum then also check the number of subarrays previously having a sum equal to 0. Excluding those subarrays from the current subarray gives new subarrays having the desired sum. Increase the count by the number of subarrays having sum 0 in that case.


# STEPS--

# 1) First, we will declare a map to store the prefix sums and their counts.

# 2) Then, we will set the value of 0 as 1 on the map.

# 3) Then we will run a loop(say i) from index 0 to n-1(n = size of the array).

# 4) For each index i, we will do the following:

#    a) We will add the current element i.e. arr[i] to the prefix sum.

#    b) We will calculate the prefix sum i.e. x-k, for which we need the occurrence.

#    c) We will add the occurrence of the prefix sum x-k i.e. mpp[x-k] to our answer.

#    d) Then we will store the current prefix sum in the map increasing its occurrence by 1.

# Question: Why do we need to set the value of 0?

# Let’s understand this using an example. Assume the given array is [3, -3, 1, 1, 1] and k is 3. Now, for index 0, we get the total prefix sum as 3, and k is also 3. So, the prefix sum of the remove-part should be x-k = 3-3 = 0. Now, if the value is not previously set for the key 0 in the map, we will get the default value 0 for the key 0 and we will add 0 to our answer. This will mean that we have not found any subarray with sum 3 till now. But this should not be the case as index 0 itself is a subarray with sum k i.e. 3.
# So, in order to avoid this situation we need to set the value of 0 as 1 on the map beforehand.


# CODE--


from collections import defaultdict

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr) # size of the given array.
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1 # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += arr[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)


# Output: The number of subarrays is: 2

# Complexity Analysis--

# Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
    
# Reason: For example, if we are using an unordered_map data structure in C++ the time complexity will be O(N) but if we are using a map data structure, the time complexity will be O(N*logN). The least complexity will be O(N) as we are using a loop to traverse the array.

# Space Complexity: O(N) as we are using a map data structure.