# METHOD- CHECKING THE COUNT OF SET BITS-

# All power of two numbers has only a one-bit set. So count the no. of set bits and if you get 1 then the number is a power of 2

# CODE-

def isPowerOfTwo(n):
    cnt = 0
    while n > 0:
        if n & 1 == 1:
            cnt = cnt + 1
        n = n >> 1
 
    if cnt == 1:
        return 1
    return 0
 
 
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


# Time complexity: O(log N)
# Auxiliary Space: O(1)        

