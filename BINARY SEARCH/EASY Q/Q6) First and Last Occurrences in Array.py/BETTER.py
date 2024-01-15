# METHOD (USING UPPER AND LOWER BOUND)--

# We are going to solve this problem using the concepts of binary search algorithms.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we can either write the codes from scratch based on the Binary Search algorithm or we can use the lower bound and the upper bound algorithm to do the same.

# In the preceding articles, we have discussed the Lower Bound and the Upper Bound algorithm in detail. Lower bound returns an index, ind, such that arr[ind] >= x(i.e. target element), and similarly, the upper bound returns the index of the first element that is greater than the target element i.e. arr[ind] > x.

# For example, if the given array is {2, 4, 6, 8, 8, 8, 11, 13}, and the target k = 8, the lower bound of 8 will be at index 3(lb), and the upper bound will return index 6(ub). 

# Therefore,
# the first occurrence of the element = lb(the index returned by lower bound)
# and the last occurrence = (ub-1)(ub = the index returned by upper bound).

# There are some edge cases.

# Edge Case 1: If the element is not present in the array.

# If the target number is not present in the array, the lower bound will return the index of the nearest greater element. So, in the code, we have to check the following:
# If arr[lb] != k: The element is not present in the array and so, there will be no first or last occurrences. So, we will return -1.
# Edge Case 2: If the element is not present in the array and all the array elements are smaller than the target number.

# In this case, lower bound will return the imaginary index n i.e. the size of the array. We need to handle this case in our code as well.
# If lb == n: No first or last occurrence exists. So, we will return -1.
# Note: Based on the index returned by the lower bound, we will decide if we need to calculate the upper bound because the absence of the first occurrence will guarantee that there will be no last occurrence.


# STEPS--

# 1) We will first calculate the index of the first occurrence(lb) using the lower bound ().

# 2) If lb == n or arr[lb] != k: We will return -1.

# 3) Otherwise, We will calculate the upper bound i.e. ub using the upper bound (). Therefore, the last occurrence = ub-1.

# 4) Finally, we will return to the first and last positions of the target.

# CODE--

def upperBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] > x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def lowerBound(arr, n, x):
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right
    return ans

def firstAndLastPosition(arr, n, k):
    lb = lowerBound(arr, n, k)
    if lb == n or arr[lb] != k:
        return (-1, -1)
    ub = upperBound(arr, n, k)
    return (lb, ub - 1)

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = firstAndLastPosition(arr, n, k)
    print("The first and last positions are:", ans[0], ans[1])



# Output: The first and last positions are: 3 5

# Complexity Analysis--

# Time Complexity: O(2*logN), where N = size of the given array.
# Reason: We are basically using a lower-bound and upper-bound algorithm.

# Space Complexity: O(1) as we are using no extra space.