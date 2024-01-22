# METHOD (USING BINARY SEARCH)--

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we are not given any sorted array on which we can apply binary search. Upon closer observation, we can recognize that our answer space, represented as [max(weights[]), sum(weights[])], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEPS--

# 1) First, we will find the maximum element i.e. max(weights[]), and the summation i.e. sum(weights[]) of the given array.

# 2) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(weights[]) and the high will point to sum(weights[]).

# 3) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 4) Eliminate the halves based on the number of days required for the capacity ‘mid’:
# We will pass the potential capacity, represented by the variable ‘mid’, to the ‘findDays()‘ function. This function will return the number of days required to ship all the weights for the particular capacity, ‘mid’.

#         A) If munerOfDays <= d: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

#         B) Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

# 5) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.


# CODE--

def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # Size of array
    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # Move to next day
            load = weights[i]  # Load the weight
        else:
            # Load the weight on the same day
            load += weights[i]
    return days

def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)


# Output:The minimum capacity should be: 9.

# Complexity Analysis--

# Time Complexity: O(N * log(sum(weights[]) – max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
# Reason: We are applying binary search on the range [max(weights[]), sum(weights[])]. For every possible answer ‘mid’, we are calling findDays() function. Now, inside the findDays() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.


