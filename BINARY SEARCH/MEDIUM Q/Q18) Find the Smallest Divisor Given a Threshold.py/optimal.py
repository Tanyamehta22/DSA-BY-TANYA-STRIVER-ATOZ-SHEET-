# METHOD (USING BINARY SEARCH)--

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now, we are not given any sorted array on which we can apply binary search. Upon closer observation, we can recognize that our answer space, represented as [1, max(arr[])], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEPS--

# 1) If n > threshold: If the minimum summation i.e. n > threshold value, the answer does not exist. In this case, we will return -1.

# 2) Next, we will find the maximum element i.e. max(arr[]) in the given array.

# 3) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 1 and the high will point to max(arr[]).

# 4) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 5) Eliminate the halves based on the summation of division results:
# We will pass the potential divisor, represented by the variable ‘mid’, to the ‘sumByD()‘ function. This function will return the summation result of the division values.

#         A) If result <= threshold: On satisfying this condition, we can conclude that the number ‘mid’ is one of our possible answers. But we want the minimum number. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

#         B) Otherwise, the value mid is smaller than the number we want. This means the numbers greater than ‘mid’ should be considered and the right half of ‘mid’ consists of such numbers. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

# 6) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.



# ** The algorithm for sumByD() is given below: **

# sumByD(arr[], div):

# arr[] -> the given array, div -> the divisor.

# 1) We will run a loop to iterate over the array.

# 2) We will divide each element by ‘div’, and consider the ceiling value.

# 3) With that, we will sum up the ceiling values as well.

# 4) Finally, we will return the summation. 

# CODE--

import math

def sumByD(arr, div):
    n = len(arr)  # size of array
    # Find the summation of division values
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum

def smallestDivisor(arr, limit):
    n = len(arr)
    if n > limit:
        return -1
    low = 1
    high = max(arr)

    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= limit:
            high = mid - 1
        else:
            low = mid + 1
    return low

arr = [1, 2, 3, 4, 5]
limit = 8
ans = smallestDivisor(arr, limit)
print("The minimum divisor is:", ans)



# Output:The minimum divisor is: 3

# Complexity Analysis--

# Time Complexity: O(log(max(arr[]))*N), where max(arr[]) = maximum element in the array, N = size of the array.
# Reason: We are applying binary search on our answers that are in the range of [1, max(arr[])]. For every possible divisor ‘mid’, we call the sumByD() function. Inside that function, we are traversing the entire array, which results in O(N).

# Space Complexity: O(1) as we are not using any extra space to solve this problem.