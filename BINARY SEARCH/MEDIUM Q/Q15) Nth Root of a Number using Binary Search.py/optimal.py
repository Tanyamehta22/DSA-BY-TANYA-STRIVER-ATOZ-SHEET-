# METHOD (USING BINARY SEARCH)--

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we are not given any sorted array on which we can apply binary search. But, if we observe closely, we can notice that our answer space i.e. [1, n] is sorted. So, we will apply binary search on the answer space.

# Edge case: How to eliminate the halves:

# Our first approach should be the following:

# After placing low at 1 and high m, we will calculate the value of ‘mid’.
# Now, based on the value of ‘mid’ raised to the power n, we will check if ‘mid’ can be our answer, and based on this value we will also eliminate the halves. If the value is smaller than m, we will eliminate the left half and if greater we will eliminate the right half.
# But, if the given numbers m and n are big enough, we cannot store the value midn in a variable. So to resolve this problem, we will implement a function like the following:

# func(n, m, mid):

# We will first declare a variable ‘ans’ to store the value midn.
# Now, we will run a loop for n times to multiply the ‘mid’ n times with ‘ans’. 
# Inside the loop, if at any point ‘ans’ becomes greater than m, we will return 2.
# Once the loop is completed, if the ‘ans’ is equal to m, we will return 1.
# If the value is smaller, we will return 0.
# Now, based on the output of the above function, we will check if ‘mid’ is our possible answer or we will eliminate the halves. Thus we can avoid the integer overflow case.

# STEPS--

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to m.

# 2) Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Eliminate the halves accordingly: 

#         A) If func(n, m, mid) == 1: On satisfying this condition, we can conclude that the number ‘mid’ is our answer. So, we will return to ‘mid’.

#         B) If func(n, m, mid) == 0: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

#         C) If func(n, m, mid) == 2: the value mid is larger than the number we want. This means the numbers greater than ‘mid’ will not be our answers and the right half of ‘mid’ consists of such numbers. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

# 4) Finally,  if we are outside the loop, this means no answer exists. So, we will return -1.

# The steps from 2-3 will be inside a loop and the loop will continue until low crosses high.

# CODE--

def func(mid, n, m):
    ans = 1
    for i in range(1, n + 1):
        ans *= mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0

def NthRoot(n: int, m: int) -> int:
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)


# Output: The peak is at index: 7

# Complexity Analysis--

# Time Complexity: O(logN), N = size of the given array.
# Reason: We are basically using binary search to find the minimum.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).