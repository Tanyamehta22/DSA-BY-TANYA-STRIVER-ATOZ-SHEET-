# METHOD(Code written from scratch using Binary Search)--

# We will basically implement 2 binary searches to find the first and the last occurrence. 

# STEPS--

# firstOccurrence():

# We will declare the 2 pointers and a ‘first’ variable initialized to -1(as If we don’t find any index, we will return -1).

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.

# 2) Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Compare arr[mid] with k: With comparing arr[mid] to k, we can observe 3 different cases:

#     A) Case 1 – If arr[mid] == k: This condition means that the index mid may be an answer. So, we will update the ‘first’ variable with mid and search in the left half if there is any smaller index that satisfies the same condition as we want the ‘first’ variable to be as minimum as possible.

#     B) Case 2 – If arr[mid] < k: In this case, mid cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.

#     C) Case 3: If arr[mid] > k: In this case, mid cannot be our answer and we need to find some smaller element. So, we will eliminate the right half and search in the left half for the answer.

# The above process will continue until the pointer low crosses high.

# Note: If the firstOccurrence() function returns a value of -1, it indicates that the target element is not found in the array. In such a scenario, there is no need to proceed with the lastOccurrence() function. We can directly conclude that the element is not present and return -1 from this step.

# lastOccurrence():

# We will declare the 2 pointers and a ‘last’ variable initialized to -1(as If we don’t find any index, we will return -1).

# Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.
# Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)
# Compare arr[mid] with k: With comparing arr[mid] to k, we can observe 3 different cases:
# Case 1 – If arr[mid] == k: This condition means that the index mid may be an answer. So, we will update the ‘last’ variable with mid and search in the right half if there is any larger index that satisfies the same condition as we want the ‘last’ variable to be as maximum as possible.
# Case 2 – If arr[mid] < k: In this case, mid cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.
# Case 3: If arr[mid] > k: In this case, mid cannot be our answer and we need to find some smaller element. So, we will eliminate the right half and search in the left half for the answer.
# The above process will continue until the pointer low crosses high. Finally, we will return the ‘first’ and the ‘last’ variables.

# CODE--

def firstOccurrence(arr, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(arr, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last


def firstAndLastPosition(arr, n, k):
    first = firstOccurrence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, k)
    return (first, last)

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    k = 8
    ans = firstAndLastPosition(arr, n, k)
    print("The first and last positions are:", ans[0], ans[1])




# Output: The first and last positions are: 3 5

# Complexity Analysis--

# Time Complexity: O(2*logN), where N = size of the given array.
# Reason: We are basically using the binary search algorithm twice.

# Space Complexity: O(1) as we are using no extra space.
