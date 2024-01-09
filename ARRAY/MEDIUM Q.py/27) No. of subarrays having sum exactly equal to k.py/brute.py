# METHOD--

# 1) First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).

# 2) Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).

# 3) After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the sum of all the elements(of that particular subarray).
                                    
# 4) After calculating the sum, we will check if the sum is equal to the given k. If it is, we will increase the value of the count.

# CODE--

def findAllSubarraysWithGivenSum(arr, k):
    n = len(arr)  # size of the given array.
    cnt = 0  # Number of subarrays.

    for i in range(n):  # starting index i.
        for j in range(i, n):  # ending index j.
            # calculate the sum of subarray [i...j].
            subarray_sum = sum(arr[i:j+1])

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
    
# Time Complexity: O(N3), where N = size of the array.
# Reason: We are using three nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N3).

# Space Complexity: O(1) as we are not using any extra space.