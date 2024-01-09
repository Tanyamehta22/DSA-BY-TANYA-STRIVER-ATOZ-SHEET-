# METHOD--

# Use two loops. The outer loop runs from 0 to size – 1 and one by one pick all elements from left to right. The inner loop compares the picked element to all the elements on its right side. If the picked element is greater than all the elements to its right side, then the picked element is the leader. 

# STEPS--

# 1)We run a loop from the first index to the 2nd last index.

#     A) And for each index, we run another loop from the next index to the last index.

#     B) If all the values to the right of that index are smaller than the index, we simply add the value in our answer data structure. 

# CODE---

def printLeaders(arr,size):
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
                break
        # Edge case for last element which will always be included   
        if j == size-1:
            print(arr[i], end=" ")

# Driver function 
arr=[16, 17, 4, 3, 5, 2] 
printLeaders(arr, len(arr))


# Output-
# 17 5 2 

# Time Complexity: O(N * N)
# Auxiliary Space: O(1)