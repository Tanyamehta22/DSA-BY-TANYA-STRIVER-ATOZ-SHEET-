# METHOD-( Sorting and Two-Pointers technique)--
# The idea is to use the two-pointer technique. But for using the two-pointer technique, the array must be sorted. Once the array is sorted the two pointers can be taken which mark the beginning and end of the array respectively. If the sum is greater than the sum of those two elements, shift the right pointer to decrease the value of the required sum and if the sum is lesser than the required value, shift the left pointer to increase the value of the required sum.

# STEPS--
 
# 1) hasArrayTwoCandidates (A[], ar_size, sum)

# 2) Sort the array in non-decreasing order.

# 3) Initialize two index variables to find the candidate 
# elements in the sorted array.

#    A) Initialize first to the leftmost index: l = 0
#    B)Initialize second the rightmost index: r = ar_size-1

# 4) Loop while l < r. 

#    A) If (A[l] + A[r] == sum) then return 1
#    B) Else if( A[l] + A[r] < sum ) then l++
#    C)Else r–

# 5) No candidates in the whole array – return 0

# CODE--

def hasArrayTwoCandidates(A, arr_size, sum):

    # sort the array
    quickSort(A,0,arr_size-1)
    l=0
    r=arr_size-1

    # traverse the array for the two elements
    while l<r:
        if (A[l]+ A[r] == sum):
            return 1
        elif (A[l]+A[r]<sum):
            l+=1
        else:
            r-=1
    return 0  

# Implementation of Quick Sort
# A[] --> Array to be sorted
# si  --> Starting index
# ei  --> Ending index
 
 
def quickSort(A, si, ei):
    if si < ei:
        pi = partition(A, si, ei)
        quickSort(A, si, pi-1)
        quickSort(A, pi + 1, ei)
 
# Utility function for partitioning
# the array(used in quick sort)
        
def partition(A, si, ei):
    x = A[ei]
    i = (si-1)
    for j in range(si, ei):
        if A[j] <= x:
            i += 1
 
            # This operation is used to swap
            # two variables is python
            A[i], A[j] = A[j], A[i]
 
        A[i + 1], A[ei] = A[ei], A[i + 1]
 
    return i + 1 

# Driver program to test the functions
A = [1, 4, 45, 6, 10, -8]
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Yes")
else:
    print("No")    

# Output--
# Yes

# Time Complexity: O(NlogN), Time complexity for sorting the array
# Auxiliary Space: O(1)       
           