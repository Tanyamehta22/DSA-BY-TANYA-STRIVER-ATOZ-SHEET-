# METHOD---

# 1)Set an integer i = 0 to denote the current index being searched.

# 2)Check if i is the last index, return arr[i].

# 3)Increment i and call the recursive function for the new value of i.

# 4)Compare the maximum value returned from the recursion function with arr[i].

# 5)Return the max between these two from the current recursion call.

# CODE---

import math

# Function to find the largest element
def largest(ar,n,i):

     # Last index return the element
    if (i==n-1):
        return arr[i]
    
    # Find the maximum from rest of the array
    recMax= largest(arr,n,i+1)

    # Compare with i-th element and return
    return max(recMax,arr[i])

# DRIVER CODE--
if __name__=='__main__':
    arr =[10,324,45,90,9808]
    n=len(arr)

    #  Function call
    print("Largest in given array is " + str(largest(arr, n, 0)))





# Output--
# Largest in given array is 9808

# Time Complexity: O(N), where N is the size of the given array. 

# Auxiliary Space: O(N), for recursive calls
