# METHOD--Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

# --Advantages of Selection Sort Algorithm
# Simple and easy to understand.
# Works well with small datasets.


# --Disadvantages of the Selection Sort Algorithm
# Selection sort has a time complexity of O(n^2) in the worst and average case.
# Does not work well on large datasets.
# Does not preserve the relative order of items with equal keys which means it is not stable.

# CODE--
import sys
A= [64,25,12,22,11]

# Traverse through all array elemets
for i in range(len(A)):

    # find the minimum element in remaining unsorted array
    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx =j

    # Swap the found minimum element with the first element
    A[i],A[min_idx] = A[min_idx], A[i]    

# DRIVER CODE-
print("sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ,")    


# Output-
# Sorted array: 
# 11 12 22 25 64 


# Complexity Analysis of Selection Sort----
    
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:
# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
    

# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 






