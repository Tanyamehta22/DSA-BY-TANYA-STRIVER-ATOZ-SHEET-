# METHOD---(USING XOR)

# The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence. The idea is based on the following two facts. 

#  XOR of a number with itself is 0. 
# XOR of a number with 0 is number itself.

# CODE--

# function to find the once  
# appearing element in array 
def find_single(ar,n):
    res=ar[0]

    # Do XOR of all elements and return 
    for i in range(1,n):
        res=res^ar[i]

    return res

# Driver code 
ar = [2, 3, 5, 4, 5, 3, 4] 
print("Element occurring once is", find_single(ar, len(ar))) 


# Output----
# Element occurring once is 2

# Time Complexity: O(n)
# Auxiliary Space: O(1)
