# METHOD ( USING IN-BUILD SQRT() FUNCTION):

# A straightforward solution to this problem is to utilize the built-in sqrt() function. This approach doesn’t require any code implementation but serves as one of the possible solutions.

# CODE--

import math

def floorSqrt(n):
    ans = int(math.sqrt(n))
    return ans

n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)



# Output: Output: The floor of square root of 28 is: 5

# Complexity Analysis--

# Time Complexity: O(logN), N = size of the given array.
# Reason: We are basically using the Binary Search algorithm.

# Space Complexity: O(1) as we are not using any extra space.