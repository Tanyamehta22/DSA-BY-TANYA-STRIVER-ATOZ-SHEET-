# METHOD-

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Upon closer observation, we can recognize that our answer space, represented as [1, (max(stalls[])-min(stalls[]))], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEP-

# 1) First, we will sort the given stalls[] array.

# 2) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to (stalls[n-1]-stalls[0]). As the ‘stalls[]’ is sorted, ‘stalls[n-1]’ refers to the maximum, and ‘stalls[0]’ is the minimum element.

# 3) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 4) Eliminate the halves based on the boolean value returned by canWePlace():
# We will pass the potential distance, represented by the variable ‘mid’, to the ‘canWePlace()‘ function. This function will return true if it is possible to place all the cows with a minimum distance of ‘mid’.

#         A) If the returned value is true: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the maximum number. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

#         B) Otherwise, the value mid is greater than the distance we want. This means the numbers greater than ‘mid’ should not be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

# 5) Finally, outside the loop, we will return the value of high as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.

# Note: It is always the opposite polarity. Initially the pointer ‘high’ was in the ‘not-possible’ half and so it ends up in the ‘possible’ half. Similarly, ‘low’ was initially in the ‘possible’ part and it ends up in the ‘not-possible’ part.

# CODE-

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
    stalls.sort()  # sort the stalls

    low = 1
    high = stalls[n - 1] - stalls[0]
    # apply binary search
    while low <= high:
        mid = (low + high) // 2
        if canWePlace(stalls, mid, k):
            low = mid + 1
        else:
            high = mid - 1
    return high

stalls = [0, 3, 4, 7, 10, 9]
k = 4
ans = aggressiveCows(stalls, k)
print("The maximum possible minimum distance is:", ans)


# Output:The maximum possible minimum distance is: 3.

# Complexity Analysis--

# Time Complexity: O(NlogN) + O(N * log(max(stalls[])-min(stalls[]))), where N = size of the array, max(stalls[]) = maximum element in stalls[] array, min(stalls[]) = minimum element in stalls[] array.
# Reason: O(NlogN) for sorting the array. We are applying binary search on [1, max(stalls[])-min(stalls[])]. Inside the loop, we are calling canWePlace() function for each distance, ‘mid’. Now, inside the canWePlace() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

