# METHOD--
# Create a new array and store the unique elements in the new array. For checking duplicate elements, just check two adjacent elements are equal or not because the array is sorted.

# STEPS---

# 1)Create an auxiliary array temp[] to store unique elements.

# 2)Traverse input array and one by one copy unique elements of arr[] to temp[]. 
#  A)Also, keep track of the count of unique elements. Let this count be j.

# 3)Copy j elements from temp[] to arr[] and return j.

# CODE--

 
# This function returns new size of modified array
def removeDuplicate(arr,n):

    # Return, if array is empty or contains
    # a single element
    if n==0 or n==1:
        return n
    temp=list(range(n))

     # Start traversing elements
    j=0
    for i in range(0,n-1):

        # If current element is not equal to next
        # then store that current element
        if arr[i]!=arr[i+1]:
            temp[j]=arr[i]
            j+=1

    # Store the last element as whether it is unique
    # or repeated, it isn't stored previously
    temp[j]=arr[n-1]
    j+=1

    # Modify original array
    for i in range(0,j):
        arr[i]=temp[i]
    return j

# Driver code--
if __name__ == '__main__':
    arr=[1,2,2,3,4,4,4,5,5]
    n=len(arr)

    # removeDuplicate() returns new size of array.
    n=removeDuplicate(arr,n)



# Output--
# 1 2 3 4 5 

# Time Complexity: O(N) 
# Auxiliary Space: O(N)








    
    # Print updated array
    for i in range(n):
        print("%d" %(arr[i]), end=" ")    



 