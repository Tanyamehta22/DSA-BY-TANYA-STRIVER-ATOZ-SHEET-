# METHOD--

# The approach is simple. We will linearly search the entire array, and try to increase the counter whenever we get the target value in the array. Using a for loop that runs from 0 to n – 1, containing an if the condition that checks whether the value at that index equals target. If true then increase the counter, at last return the counter.

# CODE--

def count(arr: [int], n: int, x: int) -> int:
    cnt = 0
    for i in range(n):
        if arr[i] == x:
            cnt += 1
    return cnt

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    x = 8
    ans = count(arr, n, x)
    print("The number of occurrences is:", ans)




# Output: The number of occurrences is: 3

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array
# Reason: We are traversing the whole array.

# Space Complexity: O(1) as we are not using any extra space.    