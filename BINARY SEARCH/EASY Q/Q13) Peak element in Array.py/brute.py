# METHOD--

# A simple approach involves iterating through the array and checking specific conditions for each element to determine the peak. By considering all the necessary conditions, including edge cases, our final condition can be summarized as follows:
# If ((i == 0 or arr[i-1] < arr[i]) and (i == n-1 or arr[i] > arr[i+1])), we have found a peak. In such cases, we can return the index of the element satisfying this condition.

# STEPS--

# 1) We will start traversing the array and for every index, we will check the below condition.

# 2) If((i == 0 or arr[i-1] < arr[i]) and (i == n-1 or arr[i] > arr[i+1])): whenever this condition is true for an element, we should return its index.
# also update the ‘index’ variable with the corresponding index value, ‘i’.

# 3)Finally, we will return ‘index’ as our answer.

# CODE--

def findPeakElement(arr: [int]) -> int:
    n = len(arr) # Size of the array

    for i in range(n):
        # Checking for the peak:
        if (i == 0 or arr[i - 1] < arr[i]) and (i == n - 1 or arr[i] > arr[i + 1]):
            return i

    # Dummy return statement
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)



# Output: The peak is at index: 7

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We are traversing the entire array.

# Space Complexity: O(1) as we are not using any extra space.


