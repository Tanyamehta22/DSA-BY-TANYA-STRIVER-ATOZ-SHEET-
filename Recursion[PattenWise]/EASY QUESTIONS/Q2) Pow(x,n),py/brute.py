# METHOD-

# A simple solution to calculate pow(x, n) would multiply x exactly n times. We can do that by using a simple for loop

# CODE-

def power(x, n):
 
    # initialize result by 1
    pow = 1
 
    # Multiply x for n times
    for i in range(n):
        pow = pow * x
 
    return pow
 
 
# Driver code
if __name__ == '__main__':
 
    x = 2
    n = 3
 
       # Function call
    print(power(x, n))


# Output
# 8

# Time Complexity: O(n)
# Auxiliary Space: O(1)    