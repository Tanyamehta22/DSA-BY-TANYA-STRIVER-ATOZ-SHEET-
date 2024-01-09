# METHOD--

# 1) First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = array size).

# 2) Inside the loop, we will run another loop(say j) that will signify the ending index as well as the current element of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).

# 3) Inside loop j, we will add the current element to the sum of the previous subarray i.e. sum = sum + arr[j].

# 4) After calculating the sum, we will check if the sum is equal to the given k. If it is, we will increase the value of the count.

# CODE--

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        subarray_sum = 0
        for j in range(i, n):  # ending index j.
            # calculate the sum of subarray [i...j]
            # sum of [i..j-1] + arr[j]
            subarray_sum += arr[j]

            # Increase the count if sum == k.
            if subarray_sum == k:
                cnt += 1

    return cnt

if __name__ == '__main__':
    arr = [3, 1, 2, 4]
    k = 6
    cnt = findAllSubarraysWithGivenSum(arr, k)
    print("The number of subarrays is:", cnt)


# Output: The number of subarrays is: 2

# Complexity Analysis--

# Time Complexity: O(N2), where N = size of the array.
# Reason: We are using two nested loops here. As each of them is running for exactly N times, the time complexity will be approximately O(N2).

# Space Complexity: O(1) as we are not using any extra space.