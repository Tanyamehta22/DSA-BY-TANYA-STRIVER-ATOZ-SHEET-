# METHOD-2( SPACE- O(1))--

# The idea is to process the array from left to right. While processing, find the first out-of-place element in the remaining unprocessed array. An element is out of place if it is negative and at odd index (0-based index), or if it is positive and at even index (0-based index). Once we find an out-of-place element, we find the first element after it with an opposite sign. We right rotate the subarray between these two elements (including these two).

# STEPS--

# 1) Maintain a variable to mark if the element is in its correct position or not. Let the variable be outofplace. Initially, it is -1.

# 2) We will iterate over the array.

# 3) If outofplace is -1, we will check if the current index is out of place.

#     A) If the current index is out of place we will update the outofplace with the index value.

#     B) Else we will keep the value as it is.

# 4) If the outofplace is not -1, we will search for the next index which has a different sign than that of the value that is present in outofplace position.

# 5) Now we will pass this two positions to right rotate our array.

# 6) Update the value of outofplace by 2 unit (becuase previously valid elements will now become the out-of-place elements).


# CODE--

# rotates the array to right by once
# from index 'outOfPlace to cur'
def rightRotate(arr,n,outOfPlace,cur):
    temp=arr[cur]
    for i in range(cur, outOfPlace,-1):
        arr[i]= arr[i-1]
    arr[outOfPlace]=temp
    return arr


def rearrange(arr,n):
    outOfPlace=-1
    for index in range(n):
        if (outOfPlace >=0):
            # if element at outOfPlace place in
            # negative and if element at index
            # is positive we can rotate the
            # array to right or if element
            # at outOfPlace place in positive and
            # if element at index is negative we
            # can rotate the array to right
            if((arr[index] >= 0 and arr[outOfPlace] < 0) or
               (arr[index] < 0 and arr[outOfPlace] >= 0)):
                arr = rightRotate(arr, n, outOfPlace, index)
                if(index-outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace = - 1

        if(outOfPlace == -1):
 
            # conditions for A[index] to
            # be in out of place
            if((arr[index] >= 0 and index % 2 == 0) or
               (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr            

# Driver Code
arr = [-5, -2, 5, 2, 4,
       7, 1, 8, 0, -8]
 
print("Given Array is:")
print(arr)
 
print("\nRearranged array is:")
print(rearrange(arr, len(arr)))



# Output---
# Given array is 
# -5 -2 5 2 4 7 1 8 0 -8 
# Rearranged array is 
# -5 5 -2 2 -8 4 7 1 8 0 

# Time Complexity: O(N^2), as we are using a loop to traverse N times and calling function to right rotate each time which will cost O (N).

# Auxiliary Space: O(1).




