# METHOD (Brian Kernighan’s Algorithm: )-

# Subtracting 1 from a decimal number flips all the bits after the rightmost set bit(which is 1) including the rightmost set bit. 

# So if we subtract a number by 1 and do it bitwise & with itself (n & (n-1)), we unset the rightmost set bit. If we do n & (n-1) in a loop and count the number of times the loop executes, we get the set bit count. 



# STEPS-

# 1  Initialize count: = 0

# 2  If integer n is not zero
#       (a) Do bitwise & with (n-1) and assign the value back to n
#           n: = n&(n-1)
#       (b) Increment count by 1
#       (c) go to step 2

# 3  Else return count



# CODE-

def countSetBits(n):
 
    count = 0
    while (n):
        n &= (n-1) 
        count+= 1
     
    return count
 
 
# Program to test function countSetBits 
i = 9
print(countSetBits(i))




# Output-
# 2

# Time Complexity: O(log n)

# Auxiliary Space: O(1)