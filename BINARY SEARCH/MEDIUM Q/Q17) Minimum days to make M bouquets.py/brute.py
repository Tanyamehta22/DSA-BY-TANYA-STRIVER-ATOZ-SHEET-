# METHOD- (LINEAR SEARCH)--

# The extremely naive approach is to check all possible answers from min(arr[]) to max(arr[]). The minimum number for which possible() returns true, is our answer.
    
# STEPS--

# 1) If m*k > arr.size: This means we have insufficient flowers. So, it is impossible to make m bouquets and we will return -1.

# 2) We will run a loop(say i) from min(arr[]) to max(arr[]) to check all possible answers.

# 3) Next, we will pass each potential answer, represented by the variable ‘i’ (which corresponds to a specific day), to the ‘possible()’ function. If the function returns true, indicating that we can create ‘m’ bouquets, we will return the value of ‘i’.

# 4) Finally, if we are outside the loop, we can conclude that is impossible to make m bouquets. So, we will return -1.

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

    for i in range(mini, maxi+1):
        if possible(arr, i, m, k):
            return i
    return -1

arr = [7, 7, 7, 7, 13, 11, 12, 7]
k = 3
m = 2
ans = roseGarden(arr, k, m)
if ans == -1:
    print("We cannot make m bouquets.")
else:
    print("We can make bouquets on day", ans)



# Output: We can make bouquets on day 12.

# Complexity Analysis--

# Time Complexity: O((max(arr[])-min(arr[])+1) * N), where {max(arr[]) -> maximum element of the array, min(arr[]) -> minimum element of the array, N = size of the array}.
# Reason: We are running a loop to check our answers that are in the range of [min(arr[]), max(arr[])]. For every possible answer, we will call the possible() function. Inside the possible() function, we are traversing the entire array, which results in O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.