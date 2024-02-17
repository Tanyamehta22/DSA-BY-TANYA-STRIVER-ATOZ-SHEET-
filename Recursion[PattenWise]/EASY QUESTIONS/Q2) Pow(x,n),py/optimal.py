# METHOD-

# Program to calculate pow(x,n) using math.exp() function--

# In math library, the math.exp() function in Python is used to calculate the value of the mathematical constant e (2.71828…) raised to a given power. It takes a single argument, which is the exponent to which the constant e should be raised, and returns the result as a float. Now, if we use combination of math.log() and math.exp() function, then we can find power of any number.

# CODE-

import math
 
def calculatePower(x, n):
      ans = math.exp(math.log(x) * n)
      ans = round(ans)
      return ans
 
# Driver code
if __name__ == '__main__':
    x = 2
    n = 3
    print(calculatePower(x, n))


# Output
# Result: 8

# Complexity Analysis:

# Time Complexity: O(1), as both math.exp() and math.log() functions run on O(1) time complexity.

# Auxiliary Space: O(1), as no extra space is used.

