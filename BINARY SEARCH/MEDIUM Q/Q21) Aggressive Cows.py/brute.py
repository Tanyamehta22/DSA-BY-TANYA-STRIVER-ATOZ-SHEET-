# METHOD-

# The extremely naive approach is to check all possible distances from 1 to max(stalls[])-min(stalls[]). The maximum distance for which the function canWePlace() returns true, will be our answer.
    
# STEPS-

# 1) First, we will sort the given stalls[] array.

# 2) We will use a loop(say i) to check all possible distances.

# 3) Next, inside the loop, we will send each distance, i, to the function canWePlace() function to check if it is possible to place the cows.

#         A) We will return (i-1), where i is the minimum distance for which the function canWePlace() returns false. Because (i-1) is the maximum distance for which we can place all the cows and for the distances >= i, it becomes impossible.

# 4) Finally, if we are outside the loop, we can conclude the minimum possible distance should be max(stalls[])-min(stalls[]). And we will return this value.


# CODE--

def canWePlace(stalls, dist, cows):
    n = len(stalls)  # size of array
    cntCows = 1  # no. of cows placed
    last = stalls[0]  # position of last placed cow
    for i in range(1, n):
        if stalls[i] - last >= dist:
            cntCows += 1  # place next cow
            last = stalls[i]  # update the last location
        if cntCows >= cows:
            return True
    return False

def aggressiveCows(stalls, k):
    n = len(stalls)  # size of array
    stalls.sort()  # sort the stalls[]
    limit = stalls[n - 1] - stalls[0]
    for i in range(1, limit + 1):
        if not canWePlace(stalls, i, k):
            return i - 1
    return limit

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)


# Output:The maximum possible minimum distance is: 3.

# Complexity Analysis--

# Time Complexity: O(NlogN) + O(N *(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
# Reason: O(NlogN) for sorting the array. We are using a loop from 1 to max(stalls[])-min(stalls[]) to check all possible distances. Inside the loop, we are calling canWePlace() function for each distance. Now, inside the canWePlace() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.







