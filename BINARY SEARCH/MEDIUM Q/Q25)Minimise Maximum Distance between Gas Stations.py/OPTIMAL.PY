# METHOD (USING BINARY SEARCH)-

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Observations:

# 1) Minimum possible answer: We will get the minimum answer when we place all the gas stations in a single location. Now, in this case, the maximum distance will be 0.

# 2) Maximum possible answer: We will not place stations before the first or after the last station rather we will place stations in between the existing stations. So, the maximum possible answer is the maximum distance between two consecutive existing stations.

# From the observations, it is clear that our answer lies in the range [0, max(dist)].

# Upon closer observation, we can recognize that our answer space is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# Changes in the binary search algorithm to apply it to the decimal answer space:

# The traditional binary search algorithm used for integer answer space won’t be effective in this case. As our answer space consists of decimal numbers, we need to adjust some conditions to tailor the algorithm to this specific context. The changes are the following:

# 1) while(low <= high): The condition ‘while(low <= high)’ inside the ‘while’ loop won’t work for decimal answers, and using it might lead to a TLE error. To avoid this, we can modify the condition to ‘while(high – low > 10^(-6))‘. This means we will only check numbers up to the 6th decimal place. Any differences beyond this decimal precision won’t be considered, as the question explicitly accepts answers within 10^-6 of the actual answer.

# 2) low = mid+1: We have used this operation to eliminate the left half. But if we apply the same here, we might ignore several decimal numbers and possibly our actual answer. So, we will use this: low = mid.

# 3) high = mid-1: Similarly, We have used this operation to eliminate the right half. But if we apply the same here, we might ignore several decimal numbers and possibly the actual answer. So, we will use this: high = mid.

# We are applying binary search on the answer i.e. the possible values of distances. So, we have to figure out a way to check the number of gas stations we can place for a particular value of distance.

# How to check the number of gas stations we can place with a particular distance ‘dist’: 

# In order to find out the number of gas stations we will use the following function:

# ** numberOfGasStationsRequired(dist, arr[]): **

# 1) We will use a loop(say i) that will run from 1 to n.

# 2) For each section between i and i-1, we will do the following:

# No. of stations = (arr[i]-arr[i-1]) / dist

# 3) Let’s keep in mind a crucial edge case: if the section_length (arr[i] – arr[i-1]) is completely divisible by ‘dist’, the actual number of stations required will be one less than what we calculate.

# if (arr[i]-arr[i-1] == (No. of stations*dist): No. of stations -= 1.
    
# 4) Now, we will add the no. of stations regarding all the sections and the total will be the answer.
    
# STEPS--

# 1) First, we will find the maximum distance between two consecutive gas stations i.e. max(dist).

# 2) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to max(dist).

# 3) Now, we will use the ‘while’ loop like this: while(high – low > 10^(-6)).

# 4) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) / 2.0

# 5) Eliminate the halves based on the number of stations returned by numberOfGasStationsRequired():

# We will pass the potential value of ‘dist’, represented by the variable ‘mid’, to the ‘numberOfGasStationsRequired()‘ function. This function will return the number of gas stations we can place.

#       A) If result > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid).

#       B) Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid).

# 6) Finally, outside the loop, we can return either low or high as their difference is beyond 10^(-6). They both can be the possible answer. Here, we have returned the ‘high’.

# The steps from 4-5 will be inside a loop and the loop will continue until (low-high <= 10^(-6)).

# CODE-

def numberOfGasStationsRequired(dist, arr):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt


def minimiseMaxDistance(arr, k):
    n = len(arr)  # size of the array
    low = 0
    high = 0

    # Find the maximum distance:
    for i in range(n - 1):
        high = max(high, arr[i + 1] - arr[i])

    # Apply Binary search:
    diff = 1e-6
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = numberOfGasStationsRequired(mid, arr)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high


arr = [1, 2, 3, 4, 5]
k = 4
ans = minimiseMaxDistance(arr, k)
print("The answer is:", ans)



# Output: The answer is: 0.5

# Complexity Analysis--

# Time Complexity: O(n*log(Len)) + O(n), n = size of the given array, Len = length of the answer space.
# Reason: We are applying binary search on the answer space. For every possible answer, we are calling the function numberOfGasStationsRequired() that takes O(n) time complexity. And another O(n) for finding the maximum distance initially.

# Space Complexity: O(1) as we are using no extra space to solve this problem.


