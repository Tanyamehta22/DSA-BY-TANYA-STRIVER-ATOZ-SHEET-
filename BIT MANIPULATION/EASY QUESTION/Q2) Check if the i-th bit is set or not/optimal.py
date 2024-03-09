#  METHOD- USING LEFT SHIFT AND & OPERATOR-

# STEPS-

# 1) Left shift given number 1 by k to create a number that has only set bit as k-th bit.
# temp = 1 << k

# 2) If bitwise AND of n and temp is non-zero, then result is SET else result is NOT SET.

# CODE-

 
def isKthBitSet(n, k):
    if n & (1 << k):
        print("SET")
    else:
        print("NOT SET")
 
 
# Driver code
if __name__ == "__main__":
    n = 5
    k = 1
 
    # Function call
    isKthBitSet(n, k)



# Output-

# NOT SET


# Time Complexity: O(1)
# Auxiliary Space: O(1)    



