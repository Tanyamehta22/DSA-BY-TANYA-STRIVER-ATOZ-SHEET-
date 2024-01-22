# METHOD (USING BINARY SEARCH)--

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we are not given any sorted array on which we can apply binary search. But, if we observe closely, we can notice that our answer space i.e. [mini(arr[]), max(arr[])] is sorted. So, we will apply binary search on the answer space.

# STEPS--

# 1) If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and we will return -1.

# 2) Next, we will find the maximum element i.e. max(arr[]), and the minimum element i.e. min(arr[]) in the array.

# 3) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to min(arr[]) and the high will point to max(arr[]).

# 4) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 5) Eliminate the halves based on the value returned by possible():
# We will pass the potential answer, represented by the variable ‘mid’ (which corresponds to a specific day), to the ‘possible()’ function.

#         A) If possible() returns true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

#         B) Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

# 6) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# CODE--

def possible(arr, day, m, k):
    n = len(arr)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // k
            cnt = 0
    noOfB += cnt // k
    return noOfB >= m

def roseGarden(arr, k, m):
    val = m * k
    n = len(arr)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    # apply binary search
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, m, k):
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)



# Output:We can make bouquets on day 12

# Complexity Analysis--

# Time Complexity: O(log(max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
# Reason: We are applying binary search on our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer ‘mid’, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.