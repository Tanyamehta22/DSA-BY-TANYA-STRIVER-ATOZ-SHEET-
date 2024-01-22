# METHOD-

# We are going to use the Binary Search algorithm to optimize the approach.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Upon closer observation, we can recognize that our answer space, represented as [max(arr[]), sum(arr[])], is actually sorted. Additionally, we can identify a pattern that allows us to divide this space into two halves: one consisting of potential answers and the other of non-viable options. So, we will apply binary search on the answer space.

# STEPS-

# 1) If m > n: In this case, book allocation is not possible and so, we will return -1.

# 2) Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to max(arr[]) and the high will point to sum(arr[]).

# 3) Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:

# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 4) Eliminate the halves based on the number of students returned by countStudents():
# We will pass the potential number of pages, represented by the variable ‘mid’, to the ‘countStudents()‘ function. This function will return the number of students to whom we can allocate the books.

#         A) If students > m: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1).

#         B) Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).

# 5) Finally, outside the loop, we will return the value of low as the pointer will be pointing to the answer.

# The steps from 3-4 will be inside a loop and the loop will continue until low crosses high.

# CODE-

def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)


# Output:The answer is: 71.

# Complexity Analysis--

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.