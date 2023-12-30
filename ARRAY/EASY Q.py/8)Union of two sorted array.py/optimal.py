# METHOD-(USING 2 POINTERS)

# STEPS--

# 1) Use two index variables i and j, initial values i = 0, j = 0 
# 2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i. 
# 3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j. 
# 4) If both are same then print any of them and increment both i and j. 
# 5) Print remaining elements of the larger array.

# CODE--

# Function prints union of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printUnion(arr1,arr2,m,n):
    i,j =0,0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            print(arr1[i], end=" ")
            i+=1
        elif arr2[j]<arr1[i]:
            print(arr2[j], end=" ")
            j+=1
        else:
            print(arr2[j], end=" ")
            j+=1
            i+=1

     # Print remaining elements of the larger array
    while i<m:
        print(arr1[i],end=" " )
        i+=1

    while i<n:
        print(arr2[j],end=" " )
        j+=1

# DRIVER CODE--
arr1=[1,2,3,4,5,6]
arr2=[2,3,5,6,7]
m=len(arr1)
n=len(arr2)
printUnion(arr1,arr2,m,n)


# Output--
# 1 2 3 4 5 6 7 

# Time Complexity : O(m + n)

# Auxiliary Space: O(1)





