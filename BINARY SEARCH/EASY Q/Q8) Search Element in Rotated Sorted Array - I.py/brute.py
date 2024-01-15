# METHOD ( LINEAR SEARCH ALGO )--

# Using this method, we will traverse the array to find the location of the target value. If it is found we will simply return the index and otherwise, we will return -1.

# STEPS--

# 1) We will traverse the array and check every element if it is equal to k. If we find any element, we will return its index.

# 2) Otherwise, we will return -1.


# CODE--

def search(arr, n, k):
    for i in range(n):
        if arr[i] == k:
            return i
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)




# Output: The index is: 3

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We have to iterate through the entire array to check if the target is present in the array.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).

