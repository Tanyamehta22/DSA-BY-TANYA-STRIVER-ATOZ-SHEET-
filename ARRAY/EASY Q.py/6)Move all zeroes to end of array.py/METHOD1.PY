# METHOD--
# Traverse the given array ‘arr’ from left to right. While traversing, maintain count of non-zero elements in array. Let the count be ‘count’. For every non-zero element arr[i], put the element at ‘arr[count]’ and increment ‘count’. After complete traversal, all non-zero elements have already been shifted to front end and ‘count’ is set as index of first 0. Now all we need to do is run a loop that makes all elements zero from ‘count’ till end of the array.

# CODE---

# Function which pushes all 
# zeros to end of an array.
def pushZerosToend(arr,n):

    # Count of non-zero elements 
    count=0

    # Traverse the array. If element  
    # encountered is non-zero, then 
    # replace the element at index 
    # 'count' with this element 
    for i in range(n):
        if arr[i]!=0:

            # here count is incremented 
            arr[count]=arr[i]
            count+=1

    # Now all non-zero elements have been 
    # shifted to front and 'count' is set 
    # as index of first 0. Make all  
    # elements 0 from count to end. 
    while count<n:
        arr[count]=0
        count+=1

# DRIVER CODE--
arr=[1,9,8,4,0,0,2,7,0,6,0,9]     
n=len(arr)
pushZerosToend(arr,n)        
print("Array after pushing all zeros to end of array:") 
print(arr) 


# Output--
# Array after pushing all zeros to end of array:
# 1 9 8 4 2 7 6 9 0 0 0 0

# Time Complexity: O(n) where n is the size of elements of the input array.

# Auxiliary Space: O(1)

