# METHOD--

# A crucial observation to note is that if an element appears twice in a sequence, either the preceding or the subsequent element will also be the same. But only for the single element, this condition will not be satisfied. So, to check this the condition will be the following:

# If arr[i] != arr[i-1] and arr[i] != arr[i+1]: If this condition is true for any element, arr[i], we can conclude this is the single element.
# Edge Cases:

# If n == 1: This means the array size is 1. If the array contains only one element, we will return that element only.
# If i == 0: This means this is the very first element of the array. The only condition, we need to check is: arr[i] != arr[i+1].
# If i == n-1: This means this is the last element of the array. The only condition, we need to check is: arr[i] != arr[i-1].
# So, we will traverse the array and we will check for the above conditions.
    


# STEPS--

# 1) At first, we will check if the array contains only 1 element. If it is, we will simply return that element.

# 2) We will start traversing the array. Then for every element, we will check the following.

# 3) If i == 0: If we are at the first index, we will check if the next element is equal.

#      A) If arr[i] != arr[i+1]: This means arr[i] is the single element and so we will return arr[i].

# 4) If i == n-1: If we are at the last index, we will check if the previous element is equal.

#     A) If arr[i] != arr[i-1]: This means arr[i] is the single element and so we will return arr[i].

# 5) For the elements other than the first and last, we will check:
# If arr[i] != arr[i-1] and arr[i] != arr[i+1]: If this condition is true for any element, arr[i], we can conclude this is the single element. And we should return arr[i].

# CODE--

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    if n == 1:
        return arr[0]

    for i in range(n):
        # Check for first index
        if i == 0:
            if arr[i] != arr[i + 1]:
                return arr[i]
        # Check for last index
        elif i == n - 1:
            if arr[i] != arr[i - 1]:
                return arr[i]
        else:
            if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
                return arr[i]

    # Dummy return statement
    return -1

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)




# Output: The single element is: 4

# Complexity Analysis--
# Time Complexity: O(N), N = size of the given array.
# Reason: We are traversing the entire array.

# Space Complexity: O(1) as we are not using any extra space.