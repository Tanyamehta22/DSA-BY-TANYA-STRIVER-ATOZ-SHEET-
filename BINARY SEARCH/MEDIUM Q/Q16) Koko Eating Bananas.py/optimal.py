# METHOD (USING BINARY SERCH)--

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we are not given any sorted array on which we can apply binary search. But, if we observe closely, we can notice that our answer space i.e. [1, max(a[])] is sorted. So, we will apply binary search on the answer space.

# STEPS--

# 1) First, we will find the maximum element in the given array i.e. max(a[]).

# 2) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to max(a[]).

# 3) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 4) Eliminate the halves based on the time required if Koko eats ‘mid’ bananas/hr:

# We will first calculate the total time(required to consume all the bananas in the array) i.e. totalH using the function calculateTotalHours(a[], mid):

#         A) If totalH <= h: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

#         B) Otherwise, the value mid is smaller than the number we want(as the totalH > h). This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

# 5) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 2-4 will be inside a loop and the loop will continue until low crosses high.

# ** calculateTotalHours(a[], hourly): **

# A) a[] -> the given array

# B) Hourly -> the possible number of bananas, Koko will eat in an hour.


# 1) We will iterate every pile of the given array using a loop(say i).

# 2) For every pile i, we will calculate the hour i.e. ceil(v[i] / hourly), and add it to the total hours.

# 3) Finally, we will return the total hours.

# CODE-

import math

def findMax(v):
    maxi = float('-inf')
    n = len(v)
    # Find the maximum
    for i in range(n):
        maxi = max(maxi, v[i])
    return maxi

def calculateTotalHours(v, hourly):
    totalH = 0
    n = len(v)
    # Find total hours
    for i in range(n):
        totalH += math.ceil(v[i] / hourly)
    return totalH

def minimumRateToEatBananas(v, h):
    low = 1
    high = findMax(v)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        totalH = calculateTotalHours(v, mid)
        if totalH <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")



# Output: Koko should eat atleast 5 bananas/hr.

# Complexity Analysis--

# Time Complexity: O(N * log(max(a[]))), where max(a[]) is the maximum element in the array and N = size of the array.
# Reason: We are applying Binary search for the range [1, max(a[])], and for every value of ‘mid’, we are traversing the entire array inside the function named calculateTotalHours().

# Space Complexity: O(1) as we are not using any extra space to solve this problem.