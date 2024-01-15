# METHOD--

# The floor of x is the largest element in the array which is smaller than or equal to x( i.e. largest element in the array <= x).

# STEPS--

# We will declare the 2 pointers and an ‘ans’ variable initialized to -1 (If we don’t find any index, we will return -1).

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.

# 2) Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:

#        A) Case 1 – If arr[mid] <= x: The index arr[mid] is a possible answer. So, we will store it and will try to find a larger number that satisfies the same condition. That is why we will remove the left half and try to find the number in the right half.

#        B) Case 2 – If arr[mid] > x: arr[mid] is definitely not the answer and we need a smaller number. So, we will reduce the search space to the left half by removing the right half.

# The above process will continue until the pointer low crosses high.

# CODE--

def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans

def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    return (f)


arr = [3, 4, 4, 7, 8, 10]
n = 6
x = 5
ans = getFloorAndCeil(arr, n, x)
print("The floor and ceil are:", ans[0], ans[1])




# Output: The floor and ceil are: 4 7

# Time Complexity: O(logN), where N = size of the given array.
# Reason: We are basically using the Binary Search algorithm.

# Space Complexity: O(1) as we are using no extra space.