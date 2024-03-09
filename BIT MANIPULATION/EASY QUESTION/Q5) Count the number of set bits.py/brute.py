# METHOD-

#  Loop through all bits in an integer, check if a bit is set and if it is, then increment the set bit count.

# CODE-

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count
 
 
# Program to test function countSetBits */
i = 9
print(countSetBits(i))



# Output
# 2

# Time Complexity: O(log n) 
# Auxiliary Space: O(1)