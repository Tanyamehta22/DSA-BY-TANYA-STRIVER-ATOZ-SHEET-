# METHOD--
# The approach is pretty simple. We will use 0 as a pivot element and whenever we see a non zero element we will swap it with the pivot element. So all the non zero element will come at the beginning.

# CODE--
A=[5,6,0,4,6,0,9,0,8]
n=len(A)
j=0
for i in range(n):
    if A[i]!=0:
        #  Partitioning the array 
        A[j], A[i]= A[i],A[j]
        j+=1
# Print the array         
print(A)   


# Output---
# 5 6 4 6 9 8 0 0 0 

# Time Complexity: O(N), where N is the size of elements of the input array.
# Auxiliary Space: O(1) 
