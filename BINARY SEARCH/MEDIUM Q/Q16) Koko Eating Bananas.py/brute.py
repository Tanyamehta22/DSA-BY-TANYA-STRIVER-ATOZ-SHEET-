# METHOD-(LINEAR SEARCH)--

# The extremely naive approach is to check all possible answers from 1 to max(a[]). The minimum number for which the required time <= h, is our answer.
    
# STEPS--

# 1) First, we will find the maximum value i.e. max(a[]) in the given array.

# 2) We will run a loop(say i) from 1 to max(a[]), to check all possible answers.

# 3) For each number i, we will calculate the hours required to consume all the bananas from the pile. We will do this using the function calculateTotalHours(), discussed below.

# 4) The first i, for which the required hours <= h, we will return that value of i.


# **calculateTotalHours(a[], hourly):**

# A) a[] -> the given array

# B) Hourly -> the possible number of bananas, Koko will eat in an hour.

# 1) We will iterate every pile of the given array using a loop(say i).

# 2) For every pile i, we will calculate the hour i.e. ceil(v[i] / hourly), and add it to the total hours.

# 3) Finally, we will return the total hours.

# CODE--

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
    # Find the maximum number
    maxi = findMax(v)

    # Find the minimum value of k
    for i in range(1, maxi+1):
        reqTime = calculateTotalHours(v, i)
        if reqTime <= h:
            return i

    # Dummy return statement
    return maxi

v = [7, 15, 6, 3]
h = 8
ans = minimumRateToEatBananas(v, h)
print("Koko should eat at least", ans, "bananas/hr.")



# Output: Koko should eat atleast 5 bananas/hr.

# Complexity Analysis--

# Time Complexity: O(max(a[]) * N), where max(a[]) is the maximum element in the array and N = size of the array.
# Reason: We are running nested loops. The outer loop runs for max(a[]) times in the worst case and the inner loop runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.



