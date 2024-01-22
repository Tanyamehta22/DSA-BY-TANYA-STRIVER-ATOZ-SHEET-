# METHOD (LINEAR SEARCH)--

# We can guarantee that our answer will lie between the range from 1 to m i.e. the given number. So, we will perform a linear search on this range and we will find the number x, such that
# func(x, n) = m. If no such number exists, we will return -1.

# Note: func(x, n) returns the value of x raised to the power n i.e. xn.

# STEPS--

# 1) We will first run a loop(say i) from 1 to m.

# 2) Inside the loop we will check the following:

#     A) If func(x, n) == m: This means x is the number we are looking for. So, we will return x from this step.

#     B) If func(x, n) > m: This means we have got a bigger number than our answer and until now we have not found any number that can be our answer. In this case, our answer does not exist and we will break out from this step and return -1.

# Note: We will use the power exponential method to implement the func() function and its time complexity will be O(logN)(where N = given exponent). 


# CODE--

def func(b, exp):
    ans = 1
    base = b
    while exp > 0:
        if exp % 2:
            exp -= 1
            ans = ans * base
        else:
            exp //= 2
            base = base * base
    return ans

def NthRoot(n: int, m: int) -> int:
    for i in range(1, m + 1):
        val = func(i, n)
        if val == m:
            return i
        elif val > m:
            break
    return -1

n = 3
m = 27
ans = NthRoot(n, m)
print("The answer is:", ans)


# Output: The answer is: 3

# Complexity Analysis--

# Time Complexity: O(M), M = the given number.
# Reason: Since we are using linear search, we traverse the entire answer space.

# Space Complexity: O(1) as we are not using any extra space.