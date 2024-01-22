# METHOD--

# The extremely naive approach is to check all possible capacities from max(weights[]) to sum(weights[]). The minimum number for which the required days <= d value, will be our answer.
    
# STEPS--

# 1) We will use a loop(say cap) to check all possible capacities.

# 2) Next, inside the loop, we will send each capacity to the findDays() function to get the number of days required for that particular capacity.

# 3) The minimum number, for which the number of days <= d, will be the answer.

# CODE-

from typing import List

def findDays(weights: List[int], cap: int) -> int:
    days = 1  # First day
    load = 0
    n = len(weights)  # size of array

    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # move to next day
            load = weights[i]  # load the weight
        else:
            # load the weight on the same day
            load += weights[i]
    
    return days

def leastWeightCapacity(weights: List[int], d: int) -> int:
    # Find the maximum and the summation
    maxi = max(weights)
    summation = sum(weights)

    for i in range(maxi, summation + 1):
        if findDays(weights, i) <= d:
            return i

    # dummy return statement
    return -1

weights = [5, 4, 5, 2, 3, 4, 5, 6]
d = 5
ans = leastWeightCapacity(weights, d)
print("The minimum capacity should be:", ans)




# Output:The minimum capacity should be: 9.

# Complexity Analysis--

# Time Complexity: O(N * (sum(weights[]) – max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
# Reason: We are using a loop from max(weights[]) to sum(weights[]) to check all possible weights. Inside the loop, we are calling findDays() function for each weight. Now, inside the findDays() function, we are using a loop that runs for N times.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.

