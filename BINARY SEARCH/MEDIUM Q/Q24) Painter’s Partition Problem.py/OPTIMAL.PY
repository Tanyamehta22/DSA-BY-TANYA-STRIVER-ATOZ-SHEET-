# METHOD (USING BINARY SEARCH)-- SAME Q AS Q22 AND Q23--

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Upon closer observation, we can recognize that our answer space, represented as [max(arr[]), sum(arr[])], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEPS-

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).

# 2) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Eliminate the halves based on the number of painters returned by countPainters():
# We will pass the potential value of time, represented by the variable ‘mid’, to the ‘countPainters()‘ function. This function will return the number of painters we need to paint all the boards.

#        A) If painters > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

#        B) Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

# 4) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.

# CODE-

def countPainters(boards, time):
    n = len(boards)  # size of array
    painters = 1
    boardsPainter = 0
    for i in range(n):
        if boardsPainter + boards[i] <= time:
            # allocate board to current painter
            boardsPainter += boards[i]
        else:
            # allocate board to next painter
            painters += 1
            boardsPainter = boards[i]
    return painters

def findLargestMinDistance(boards, k):
    low = max(boards)
    high = sum(boards)
    # Apply binary search
    while low <= high:
        mid = (low + high) // 2
        painters = countPainters(boards, mid)
        if painters > k:
            low = mid + 1
        else:
            high = mid - 1
    return low

boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)



# Output:The answer is: 60.

# Complexity Analysis--

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countPainters() function for the value of ‘mid’. Now, inside the countPainters() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.
