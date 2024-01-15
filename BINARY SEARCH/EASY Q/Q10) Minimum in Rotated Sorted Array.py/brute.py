# METHOD- (LINEAR SEARCH)

# One straightforward approach, we can consider is using the linear search algorithm. Using this method, we will find the minimum number from telnetlib import WILL
# from the array.

# STEPS--

# 1) First, we will declare a ‘mini’ variable initialized with a large number.

# 2)After that, we will traverse the array and compare each element with the ‘mini’ variable. Each time the ‘mini’ variable will be updated with the minimum value i.e. min(mini, arr[i]).

# 3) Finally, we WILL return ‘mini’ as our answer.

# CODE--

import sys
def findMin(arr: [int]):
    n = len(arr)  # size of the array.
    mini = sys.maxsize
    for i in range(n):
        # Always keep the minimum.
        mini = min(mini, arr[i])
    return mini

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)



# Output: The minimum element is: 0

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We have to iterate through the entire array to check if the target is present in the array.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).