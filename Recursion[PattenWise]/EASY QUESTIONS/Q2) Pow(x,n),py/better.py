# METHOD-
# (USING DIVIDE AND CONQUEROR APPROACH)

# The problem can be recursively defined by:

# power(x, n) = power(x, n / 2) * power(x, n / 2);        // if n is even
# power(x, n) = x * power(x, n / 2) * power(x, n / 2);    // if n is odd

# CODE- (ALSO COVERS NEGATIVE X AND FLOAT Y)

# Python3 code for extended version
# of power function that can work
# for float x and negative y
 
 
def power(x, y):
 
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
 
    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0):
            return x * temp * temp
        else:
            return (temp * temp) / x
 
 
# Driver Code
if __name__ == "__main__":
    x, y = 2, -3
 
    # Function call
    print('%.6f' % (power(x, y)))
 
# Output
# 0.125

# Time Complexity: O(log |n|)
# Auxiliary Space: O(log |n|) , for recursive call stack
