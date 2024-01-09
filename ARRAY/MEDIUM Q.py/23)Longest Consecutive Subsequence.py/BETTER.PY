# METHOD (using sorting without removing duplicate elements)-

# The approach involves initially sorting the array. Next, you count the consecutive elements present in the sorted array while skipping any repeated elements.

# CODE-
def findLongestConseqSubseq(arr):
    arr.sort()
    n=len(arr)

     # If the array has only one element, the longest consecutive subsequence is 1
    if n==1:
        return 1
    
    count =1
    max_count = -1
    
    for i in range(n-1):
        # Check if the difference between the current element and the next element is 1
        if arr[i+1]- arr[i]==1:
            count+=1

        # If the difference is 0, continue to the next iteration
        elif arr[i+1] - arr[i]==0:
            continue

        # If the difference is not 1 or 0, reset the count to 1
        else:
            count=1    

        # Update max_count with the maximum value between max_count and count    
        max_count = max(max_count, count)

    return max_count    

arr = [0, 1, 1, 1, 1, 1, 2, 3]
result = findLongestConseqSubseq(arr)
print("Longest Consecutive subsequence:", result)



# Output--
# Longest Consecutive subsequence: 4


# Time Complexity: O(NlogN): Due to the sorting step, while the subsequent traversal of the sorted array only requires O(N) time.

# Space Complexity: O(1): No extra space is being used.

