# METHOD--(USING BINARY SEARCH)

# Here, we can easily observe, that we have to find the minimum in a sorted array. That is why, we can think of using the Binary Search algorithm to solve this problem.

# The primary objective of the Binary Search algorithm is to efficiently determine the appropriate half to eliminate, thereby reducing the search space by half. It does this by determining a specific condition that ensures that the target is not present in that half.

# Key Observation: If an array is rotated and sorted, we already know that for every index, one of the 2 halves of the array will always be sorted.

# Based on this observation, we adopted a straightforward two-step process to eliminate one-half of the rotated sorted array. 

# First, we identify the sorted half of the array. 
# Once found, we determine if the target is located within this sorted half. 
# If not, we eliminate that half from further consideration. 
# Conversely, if the target does exist in the sorted half, we eliminate the other half.
# Let’s observe how we identify the sorted half:

# We basically compare arr[mid] with arr[low] and arr[high] in the following way:

# If arr[low] <= arr[mid]: In this case, we identified that the left half is sorted.
# If arr[mid] <= arr[high]: In this case, we identified that the right half is sorted.
# Let’s observe how we will find the minimum element:

# In this situation, we have two possibilities to consider. The sorted half of the array may or may not include the minimum value. However, we can leverage the property of the sorted half, specifically that the leftmost element of the sorted half will always be the minimum element within that particular half.

# During each iteration, we will select the leftmost element from the sorted half and discard that half from further consideration. Among all the selected elements, the minimum value will serve as our answer.

# To facilitate this process, we will declare a variable called ‘ans’ and initialize it with a large number. Then, at each step, after selecting the leftmost element from the sorted half, we will compare it with ‘ans’ and update ‘ans’ with the smaller value (i.e., min(ans, leftmost_element)).

# Note: If, at any index, both the left and right halves of the array are sorted, we have the flexibility to select the minimum value from either half and eliminate that particular half (in this case, the left half is chosen first). The algorithm already takes care of this case, so there is no need for explicit handling.



# STEPS--

# 1) Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.

# 2) Calculate the ‘mid’: Now, inside a loop, we will calculate the value of ‘mid’ using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)

# 3) Identify the sorted half, and after picking the leftmost element, eliminate that half.

#         A) If arr[low] <= arr[mid]: This condition ensures that the left part is sorted. So, we will pick the leftmost element i.e. arr[low]. Now, we will compare it with ‘ans’ and update ‘ans’ with the smaller value (i.e., min(ans, arr[low])). Now, we will eliminate this left half(i.e. low = mid+1).

#         B) Otherwise, if the right half is sorted:  This condition ensures that the right half is sorted. So, we will pick the leftmost element i.e. arr[mid]. Now, we will compare it with ‘ans’ and update ‘ans’ with the smaller value (i.e., min(ans, arr[mid])). Now, we will eliminate this right half(i.e. high = mid-1).

# 4) This process will be inside a loop and the loop will continue until low crosses high. Finally, we will return the ‘ans’ variable that stores the minimum element.


# CODE--

import sys
def findMin(arr: [int]):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        if arr[low] <= arr[mid]:  # if left part is sorted
            ans = min(ans, arr[low])  # keep the minimum
            low = mid + 1  # eliminate left half
            
        else:  # if right part is sorted
            ans = min(ans, arr[mid])  # keep the minimum
            high = mid - 1  # eliminate right half

    return ans

if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    ans = findMin(arr)
    print("The minimum element is:", ans)



# Output: The minimum element is: 0

# Complexity Analysis--

# Time Complexity: O(logN), N = size of the given array.
# Reason: We are basically using binary search to find the minimum.

# Space Complexity: O(1)
# Reason: We have not used any extra data structures, this makes space complexity, even in the worst case as O(1).
