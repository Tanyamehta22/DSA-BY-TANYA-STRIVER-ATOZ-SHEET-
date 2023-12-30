# METHOD--

# This problem can be solved efficiently just by maintaining a separate index for the same array as maintained for different array in the previous method and replacing that element with the unique element.
    
# STEPS--

# 1)Traverse input array from i = 0 to N:
#   A)Keep track of the count of unique elements. Let this count be j.
#   B)Swap arr[j] with arr[i].

# 2)At last, return j.

# CODE--

def remove_duplicates(arr):
    n=len(arr)
    if n==0 or n==1:
        return n
    
    # To store index of next unique element
    j=0

     # Doing same as done in Method 1
    # Just maintaining another updated index i.e. j
    for i in range(n-1):
        if arr[i]!= arr[i+1]:
            arr[j] = arr[i]
            j+=1

    arr[j]=arr[n-1]

    return j+1

# Driver code--
if __name__ == '__main__':
    arr=[1,2,2,3,4,4,4,5,5]
    n=len(arr)

    # remove_duplicates() returns new size of array.
    n=remove_duplicates(arr)

    # Print updated array
    for i in range(n):
        print(arr[i], end=" ")


# Output--
# 1 2 3 4 5    

# Time Complexity: O(N) 
# Auxiliary Space: O(1)



