# METHOD-
# N & (N-1)

# CODE-

def isPowerOfTwo(x):
 
    # First x in the below expression
    # is for the case when x is 0
    return (x and (not(x & (x - 1))))
 
 
# Driver code
if __name__ == "__main__":
 
    # Function call
    if(isPowerOfTwo(31)):
        print('Yes')
    else:
        print('No')
 
    if(isPowerOfTwo(64)):
        print('Yes')
    else:
        print('No')




# Output-
# No
# Yes


# Time Complexity: O(1)
# Auxiliary Space: O(1)        