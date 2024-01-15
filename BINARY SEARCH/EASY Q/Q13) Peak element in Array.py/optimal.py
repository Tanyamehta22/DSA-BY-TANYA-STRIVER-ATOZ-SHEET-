# METHOD ( USING BINARY SEARCH )--

# REFER NOTES

# STEPS--

# Note: At the start of the algorithm, we address the edge cases of identifying the peak element without requiring separate conditions during the check for arr[mid] inside the loop. And the search space will be from index 1 to n-2 as indices 0 and n-1 have already been checked in the edge cases.

# The final steps will be as follows:

# 1) If n == 1: This means the array size is 1. If the array contains only one element, we will return that index i.e. 0.

# 2) If arr[0] > arr[1]: This means the very first element of the array is the peak element. So, we will return the index 0.

# 3) If arr[n-1] > arr[n-2]: This means the last element of the array is the peak element. So, we will return the index n-1.

# 4) Place the 2 pointers i.e. low and high: Initially, we will place the pointers excluding index 0 and n-1 like this: low will point to index 1, and high will point to index n-2 i.e. the second last index.

# 5) Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 6) Check if arr[mid] is the peak element:
# If arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]: If this condition is true for arr[mid], we can conclude arr[mid] is the peak element. We will return the index ‘mid’.
    
# 7) If arr[mid] > arr[mid-1]: This means we are in the left half and we should eliminate it as our peak element appears on the right. So, we will do this:
# low = mid+1.

# 8) Otherwise, we are in the right half and we should eliminate it as our peak element appears on the left. So, we will do this: high = mid-1. This case also handles the case for the index ‘mid’ being a common point of a decreasing and increasing sequence. It will consider the left peak and eliminate the right peak.


# The steps from 5 to 8 will be inside a loop and the loop will continue until low crosses high.

# CODE--

def findPeakElement(arr: [int]) -> int:
    n = len(arr)  # Size of the array

    # Edge cases:
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1

    low = 1
    high = n - 2
    while low <= high:
        mid = (low + high) // 2

        # If arr[mid] is the peak:
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid

        # If we are in the left:
        if arr[mid] > arr[mid - 1]:
            low = mid + 1

        # If we are in the right:
        # Or, arr[mid] is a common point:
        else:
            high = mid - 1

    # Dummy return statement
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
ans = findPeakElement(arr)
print("The peak is at index:", ans)




# Output: The peak is at index: 7

# Complexity Analysis--

# Time Complexity: O(logN), N = size of the given array.
# Reason: We are basically using binary search to find the minimum.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).