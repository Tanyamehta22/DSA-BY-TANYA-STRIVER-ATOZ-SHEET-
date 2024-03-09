# METHOD- (USING BITWISE XOR)

# The bitwise XOR operator can be used to swap two variables. The XOR of two numbers x and y returns a number that has all the bits as 1 wherever bits of x and y differ.

# For example, XOR of 10 (In Binary 1010) and 5 (In Binary 0101) is 1111, and XOR of 7 (0111) and 5 (0101) is (0010). 



# CODE-

x = 10
y = 5
 
# Code to swap 'x' and 'y'
x = x ^ y; # x now becomes 15 (1111)
y = x ^ y; # y becomes 10 (1010)
x = x ^ y; # x becomes 5 (0101)
 
print ("After Swapping: x = ", x, " y =", y)
 


# Output-
# After Swapping: x =5, y=10


# Time Complexity: O(1).
# Auxiliary Space: O(1).