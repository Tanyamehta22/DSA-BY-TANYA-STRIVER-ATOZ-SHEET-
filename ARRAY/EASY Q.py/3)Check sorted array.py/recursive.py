# METHOD--

# 1: If size of array is zero or one, return true.

# 2: Check last two elements of array, if they are
#    sorted, perform a recursive call with n-1
#    else, return false.

# If all the elements will be found sorted, n will
# eventually fall to one, satisfying Step 1.

# CODE--

# Function that returns 0 if a pair
# is found unsorted
def arraySortedOrNot(arr):
    # Calculating length
    n=len(arr)

    # Array has one or no element or the
    # rest are already checked and approved.
    if n==1 or n==0:
        return True
    
    
    # Recursion applied till last element
    return arr[0]<=arr[1] and arraySortedOrNot(arr[1:])

arr=[20,23,23,45,78,88]


# Displaying result
if arraySortedOrNot(arr):
    print("yes")
else:
    print("No")  


# Output--
# Yes

# Time Complexity: O(n)

# Auxiliary Space: O(n) for Recursion Call Stack.      

