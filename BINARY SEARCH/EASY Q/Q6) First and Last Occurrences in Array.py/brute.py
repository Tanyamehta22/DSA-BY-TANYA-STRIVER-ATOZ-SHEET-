# METHOD(USING LINEAR SEARCH)-

# Basically, we will traverse the entire array to find the first and the last occurrences.

# STEPS--

# 1) First, we will declare two variables ‘first’(to store the first occurrence) and ‘last’(to store the last occurrence). We will initialize them with -1.

# 2) We will start traversing the array using a loop. 

# 3) When we first encounter the element k in the array, we will store the index in the first and last variables.

# 4) But for the next occurrences of k, we will not update the variable ‘first’ instead, we will only update the last variable with the current index. In order to do this update, we will check the value of the variable ‘first’. If the value is -1(i.e. we are facing k for the first time), we will update both the variables, and otherwise, we will only update the variable ‘last’.

# CODE--


def firstAndLastPosition(arr, n, k):
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == k:
            if first == -1:
                first = i
            last = i
    return (first, last)

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = firstAndLastPosition(arr, n, k)
    print("The first and last positions are:", ans[0], ans[1])



# Output: The first and last positions are: 3 5

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array
# Reason: We are traversing the entire array.

# Space Complexity: O(1) as we are not using any extra space.