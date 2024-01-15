# METHOD-(LINEAR SEARCH)--

# One straightforward approach we can consider is using the linear search algorithm. Using this method, we will traverse the array to check if the target is present in the array. If it is found we will simply return True and otherwise, we will return False.

# STEPS-

# 1) We will traverse the array and check every element if it is equal to k. If we find any element, we will return True.

# 2) Otherwise, we will return False.

# CODE--

from typing import *
def searchInARotatedSortedArrayII(arr : List[int], k : int) -> bool:
    for num in arr:
        if num == k:
            return True
    return False

if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    ans = searchInARotatedSortedArrayII(arr, k)
    if not ans:
        print("Target is not present.")
    else:
        print("Target is present in the array.")



# Output: Target is present in the array.

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We have to iterate through the entire array to check if the target is present in the array.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).