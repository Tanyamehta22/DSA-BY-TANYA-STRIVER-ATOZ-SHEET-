# METHO(USING LINEAR SEARCH)--

# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.

# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.


# CODE--

def lowerBound(arr: [int], n: int, x: int) -> int:
    for i in range(n):
        if arr[i] >= x:
            #lower bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 15, 19]
    n = 5
    x = 9
    ind = lowerBound(arr, n, x)
    print("The lower bound is the index:", ind)


# Output: The lower bound is the index: 3

# Complexity Analysis--

# Time Complexity: O(N), where N = size of the given array.
# Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

# Space Complexity: O(1) as we are using no extra space.
