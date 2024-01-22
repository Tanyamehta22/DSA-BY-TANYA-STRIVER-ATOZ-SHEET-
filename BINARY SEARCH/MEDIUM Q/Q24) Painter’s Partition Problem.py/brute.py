# METHOD-

# The extremely naive approach is to check all possible answers from max(arr[]) to sum(arr[]). The minimum time for which we can paint all the boards will be our answer.
    
# STEPS-

# 1) First, we will find the maximum element and the summation of the given array.

# 2) We will use a loop(say time) to check all possible answers from max(arr[]) to sum(arr[]).

# 3) Next, inside the loop, we will send ‘time’, to the function countPainters() function to get the number of painters to whom we can allocate the boards.

#         A) The first value of ‘time’, for which the number of painters will be lesser or equal to ‘k’, will be our answer. So, we will return that particular value of ‘time’.

# 4) Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.

# CODE--

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

    for time in range(low, high+1):
        if countPainters(boards, time) <= k:
            return time
    return low


boards = [10, 20, 30, 40]
k = 2
ans = findLargestMinDistance(boards, k)
print("The answer is:", ans)



# Output: The answer is: 60

# Complexity Analysis--

# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible values of time. Inside the loop, we are calling the countPainters() function for each number. Now, inside the countPainters() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.



