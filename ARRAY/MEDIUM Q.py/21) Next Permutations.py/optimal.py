# METHOD-(REFER TO THE NOTEBOOK FOR DRY- RUN)--

# STEPS--

# 1) Iterate over the given array from end and find the first index (pivot) which doesn’t follow property of non-increasing suffix, (i.e,  arr[i] < arr[i + 1]).

# 2) Check if pivot index does not exist 

#      A) This means that the given sequence in the array is the largest as possible. So, swap the complete array.

# 3) Otherwise, Iterate the array from the end and find for the successor of pivot in suffix.

# 4) Swap the pivot and successor

# 5) Minimize the suffix part by reversing the array from pivot + 1 till N.

# CODE-

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Function to find the next permutation 
def nextPermutation(arr):
    n=len(arr)
    i=len(arr)-2
    j=0

    # Find for the pivot element.
    # A pivot is the first element from
    # end of sequencewhich doesn't follow
    # property of non-increasing suffix
    while i>=0:
        if arr[i]<arr[i+1]:
            break
        i=i-1

    # Check if pivot is not found
    if (i<0):
        arr.reverse()

    # if pivot is found
    else:
        # Find for the successor of pivot in suffix
        for j in range(n-1,i,-1):
            if(arr[j]>arr[i]):
                break

        # Swap the pivot and successor
        swapPositions(arr, i, j)
         
        # Minimise the suffix part
        # initializing range
        strt, end = i+1, len(arr)
 
        # Third arg. of split with -1 performs reverse
        arr[strt:end] = arr[strt:end][::-1]
 
# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 6, 5, 4]
     
    # Function call
    nextPermutation(arr)
     
    # Printing the answer
    for i in arr:
        print(i, end=" ")
 


# Output--
# 1 2 4 3 5 6 

# Time Complexity: O(N), where N is the size of the given array.
# Auxiliary Space: O(1)
