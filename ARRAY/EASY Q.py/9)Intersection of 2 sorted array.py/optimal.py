# METHOD 2 -- (USING 2 POINTERS)

# STEPS--

# 1)Use two index variables i and j, initial values i = 0, j = 0 

# 2) If arr1[i] is smaller than arr2[j] then increment i.

# 3) If arr1[i] is greater than arr2[j] then increment j. 

# 4) If both are same then print any of them and increment both i and j.


# CODE--

# Function prints Intersection of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printIntersection(arr1,arr2,m,n):
    i,j = 0,0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        else:
            print(arr2[j], end=" ")
            j+=1
            i+=1

 
# Driver program to test above function
arr1 = [1,2,4,5,6]
arr2=[2,3,5,7]
m=len(arr1)
n=len(arr2)
printIntersection(arr1,arr2,m,n)



# Output
# 2 5 

# Time Complexity : O(m + n)

# Auxiliary Space: O(1)




