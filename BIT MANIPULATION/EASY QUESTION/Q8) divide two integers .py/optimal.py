# METHOD- (USING BIT MANIPULATION)

# Use bit manipulation in order to find the quotient. The divisor and dividend can be written as 

# dividend = quotient * divisor + remainder



# STEPS-

# 1) Determine the most significant bit in the divisor. This can easily be calculated by iterating on the bit position i from 31 to 1.

# 2) Find the first bit for which divisor << i is less than dividend and keep updating the ith bit position for which it is true.

# 3) Add the result in the temp variable for checking the next position such that (temp + (divisor << i) ) is less than the dividend.

# 4)Return the final answer of the quotient after updating with a corresponding sign.


# CODE--

def divide(dividend, divisor):
     
    # Calculate sign of divisor 
    # i.e., sign will be negative
    # either one of them is negative
    # only if otherwise it will be
    # positive
     
    sign = (-1 if((dividend < 0) ^ 
                  (divisor < 0)) else 1);
     
    # remove sign of operands
    dividend = abs(dividend);
    divisor = abs(divisor);
     
    # Initialize
    # the quotient
    quotient = 0;
    temp = 0;
     
    # test down from the highest 
    # bit and accumulate the 
    # tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i;
            quotient |= 1 << i;
    #if the sign value computed earlier is -1 then negate the value of quotient
    if sign ==-1 :
      quotient=-quotient;
    return quotient;
 
# Driver code
a = 10;
b = 3;
print(divide(a, b));
 
a = 43;
b = -8;
print(divide(a, b));



# Output-
# 3
# -5


# Time complexity : O(log(a)) 
# Auxiliary space : O(1)


