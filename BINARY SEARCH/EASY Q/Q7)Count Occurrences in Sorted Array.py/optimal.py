# METHOD-(USING FIRST AND LAST OCCURENCES OF Q6)----

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Now in order to solve this problem, we are going to use the previous concept. We will find the first and the last occurrences and figure out the number of occurrences like the following:

# Total number of occurrences = last occurrence – first occurrence + 1


# STEPS--

# 1) We will get the first and the last occurrences of the number using the function firstAndLastPosition(). For the implementation details of the function, please refer to the previous article.

# 2) After getting the indices, we will check the following cases:

#        A) If the first index == -1: This means that the target value is not present in the array. So, we will return 0 as the answer.

#        B) Otherwise: We will find the total number of occurrences like this:
#        The total number of occurrences  = (last index – first index + 1) and return this length as the answer.



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

def count(arr: [int], n: int, x: int) -> int:
    first, last = firstAndLastPosition(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1

if __name__ == "__main__":
    arr = [2, 4, 6, 8, 8, 8, 11, 13]
    n = 8
    x = 8
    ans = count(arr, n, x)
    print("The number of occurrences is:", ans)





# Output:The number of occurrences is: 3

# Complexity Analysis--

# Time Complexity: O(2*logN), where N = size of the given array.
# Reason: We are basically using the binary search algorithm twice.

# Space Complexity: O(1) as we are using no extra space.    



