# METHOD--( THIS IS SAME AS LOWER BOUND Q3)

# STEPS--

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.

# 2) Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:

#       A) Case 1 – If arr[mid] >= x: This condition means that the index mid may be an answer. So, we will update the ‘ans’ variable with mid and search in the left half if there is any smaller index that satisfies the same condition. Here, we are eliminating the right half.

#       B) Case 2 – If arr[mid] < x: In this case, mid cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.

# CODE--

def searchInsert(arr: [int], x: int) -> int:
    n = len(arr)  # size of the array
    low = 0
    high = n - 1
    ans = n

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = mid
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans

if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6
    ind = searchInsert(arr, x)
    print("The index is:", ind)



# Output: The index is: 3

# Time Complexity: O(logN), where N = size of the given array.
# Reason: We are basically using the Binary Search algorithm.

# Space Complexity: O(1) as we are using no extra space.