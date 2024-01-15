# METHOD (USING BINARY SEARCH)--

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Observation: 

# To utilize the binary search algorithm effectively, it is crucial to ensure that the input array is sorted. By having a sorted array, we guarantee that each index divides the array into two sorted halves. In the search process, we compare the target value with the middle element, i.e. arr[mid], and then eliminate either the left or right half accordingly. This elimination becomes feasible due to the inherent property of the sorted halves(i.e. Both halves always remain sorted).

# However, in this case, the array is both rotated and sorted. As a result, the property of having sorted halves no longer holds. This disruption in the sorting order affects the elimination process, making it unreliable to determine the target’s location by solely comparing it with arr[mid].

# Key Observation: Though the array is rotated, we can clearly notice that for every index, one of the 2 halves will always be sorted. In the above example, the right half of the index mid is sorted.

# So, to efficiently search for a target value using this observation, we will follow a simple two-step process. 

# First, we identify the sorted half of the array. 
# Once found, we determine if the target is located within this sorted half. 
# If not, we eliminate that half from further consideration. 
# Conversely, if the target does exist in the sorted half, we eliminate the other half.


# STEPS--

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index, and high will point to the last index.

# 2) Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Check if arr[mid] == target: If it is, return the index mid.

# 4) Identify the sorted half, check where the target is located, and then eliminate one half accordingly:

#        A) If arr[low] <= arr[mid]: This condition ensures that the left part is sorted.

#                  A.1) If arr[low] <= target && target <= arr[mid]: It signifies that the target is in this sorted half. So, we will eliminate the right half (high = mid-1).

#                  A.2) Otherwise, the target does not exist in the sorted half. So, we will eliminate this left half by doing low = mid+1.

#         B) Otherwise, if the right half is sorted:

#                 B.1) If arr[mid] <= target && target <= arr[high]: It signifies that the target is in this sorted right half. So, we will eliminate the left half (low = mid+1).

#                 B.2) Otherwise, the target does not exist in this sorted half. So, we will eliminate this right half by doing high = mid-1.

# 5) Once, the ‘mid’ points to the target, the index will be returned.

# 6) This process will be inside a loop and the loop will continue until low crosses high. If no index is found, we will return -1.


# CODE--


def search(arr, n, k):
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2

        # if mid points the target
        if arr[mid] == k:
            return mid

        # if left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                # element exists
                high = mid - 1
            else:
                # element does not exist
                low = mid + 1
        else:  # if right part is sorted
            if arr[mid] <= k and k <= arr[high]:
                # element exists
                low = mid + 1
            else:
                # element does not exist
                high = mid - 1
    return -1

if __name__ == "__main__":
    arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    n = 9
    k = 1
    ans = search(arr, n, k)
    if ans == -1:
        print("Target is not present.")
    else:
        print("The index is:", ans)




# Output: The index is: 3

# Complexity Analysis--

# Time Complexity: O(logN), N = size of the given array.
# Reason: We are using binary search to search the target.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).