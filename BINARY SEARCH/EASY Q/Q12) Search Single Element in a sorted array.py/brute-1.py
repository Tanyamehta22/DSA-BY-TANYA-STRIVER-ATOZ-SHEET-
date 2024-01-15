# METHOD (USING XOR)--

# We can simplify the above approach using the XOR operation. We need to remember 2 important properties of XOR:

# a ^ a = 0, XOR of two same numbers results in 0.
# a ^ 0 = a, XOR of a number with 0 always results in that number.
# Now, if we XOR all the array elements, all the duplicates will result in 0 and we will be left with a single element.

# STEPS--

# 1) We will declare an ‘ans’ variable initialized with 0.

# 2) We will traverse the array and XOR each element with the variable ‘ans’.

# 3) After complete traversal, the ‘ans’ variable will store the single element and we will return it.

# CODE--

def singleNonDuplicate(arr):
    n = len(arr)  # Size of the array
    ans = 0
    # XOR all the elements
    for i in range(n):
        ans = ans ^ arr[i]
    return ans

arr = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
ans = singleNonDuplicate(arr)
print("The single element is:", ans)



# Output: The single element is: 4

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We are traversing the entire array.

# Space Complexity: O(1) as we are not using any extra space.