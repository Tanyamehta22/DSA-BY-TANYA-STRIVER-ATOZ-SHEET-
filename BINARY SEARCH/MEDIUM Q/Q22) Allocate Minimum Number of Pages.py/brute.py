# METHOD--

# The extremely naive approach is to check all possible pages from max(arr[]) to sum(arr[]). The minimum pages for which we can allocate all the books to M students will be our answer.
    
# STEPS-

# 1) If m > n: In this case, book allocation is not possible and so, we will return -1.

# 2) Next, we will find the maximum element and the summation of the given array.

# 3) We will use a loop(say pages) to check all possible pages from max(arr[]) to sum(arr[]).

# 4) Next, inside the loop, we will send each ‘pages’, to the function countStudents() function to get the number of students to whom we can allocate the books.

#        A) The first number of pages, ‘pages’, for which the number of students will be equal to ‘m’, will be our answer. So, we will return that particular ‘pages’.

# 5) Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.

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

    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
            return pages
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)



# Output: The answer is: 71.

# Complexity Analysis--

# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
# Reason: We are using a loop from max(arr[]) to sum(arr[]) to check all possible numbers of pages. Inside the loop, we are calling the countStudents() function for each number. Now, inside the countStudents() function, we are using a loop that runs for N times.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.
