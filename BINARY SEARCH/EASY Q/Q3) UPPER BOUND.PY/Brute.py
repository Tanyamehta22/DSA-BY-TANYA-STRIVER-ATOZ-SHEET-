# METHOD--

# The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.

# The upper bound is the smallest index, ind, where arr[ind] > x.

# But if any such index is not found, the upper bound algorithm returns n i.e. size of the given array. The main difference between the lower and upper bound is in the condition. For the lower bound the condition was arr[ind] >= x and here, in the case of the upper bound, it is arr[ind] > x.

# LINEAR SEARCH----

# Let’s understand how we can find the answer using the linear search algorithm. With the knowledge that the array is sorted, our approach involves traversing the array starting from the beginning. During this traversal, each element will be compared with the target value, x. The index, i, where the condition arr[i] > x is first satisfied, will be the answer.

# CODE--

def upperBound(arr: [int], x: int, n: int) -> int:
    for i in range(n):
        if arr[i] > x:
            # upper bound found
            return i
    return n

if __name__ == "__main__":
    arr = [3, 5, 8, 9, 15, 19]
    n = 6
    x = 9
    ind = upperBound(arr, x, n)
    print("The upper bound is the index:", ind)



# Output: The upper bound is the index: 4

# Complexity Analysis--

# Time Complexity: O(N), where N = size of the given array.
# Reason: In the worst case, we have to travel the whole array. This is basically the time complexity of the linear search algorithm.

# Space Complexity: O(1) as we are using no extra space.

