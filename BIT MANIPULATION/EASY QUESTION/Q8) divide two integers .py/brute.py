# METHOD-

# Keep subtracting the divisor from the dividend until the dividend becomes less than the divisor. The dividend becomes the remainder, and the number of times subtraction is done becomes the quotient.

# CODE-

def divide(dividend, divisor):
 
    # Calculate sign of divisor i.e.,
    # sign will be negative only if
    # either one of them is negative
    # otherwise it will be positive
    sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
 
    # Update both divisor and
    # dividend positive
    dividend = abs(dividend)
    divisor = abs(divisor)
 
    # Initialize the quotient
    quotient = 0
    while (dividend >= divisor):
        dividend -= divisor
        quotient += 1
 
     # if the sign value computed earlier is -1 then negate the value of quotient
 
    if sign == -1:
        quotient = -quotient
 
    return quotient
 
 
# Driver code
a = 10
b = 3
print(divide(a, b))
a = 43
b = -8
print(divide(a, b))



# Output-
# 3
# -5

# Time complexity : O(a/b) 
# Auxiliary space : O(1)