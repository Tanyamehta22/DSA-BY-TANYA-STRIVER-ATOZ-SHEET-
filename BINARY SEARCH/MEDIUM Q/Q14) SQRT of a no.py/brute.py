# METHOD (USING LINEAR SEARCH)--

# We can guarantee that our answer will lie between the range from 1 to n i.e. the given number. So, we will perform a linear search on this range and we will find the maximum number x, such that x*x <= n.

# STEPS--

# 1) We will first declare a variable called ‘ans’.

# 2) Then, we will first run a loop(say i) from 1 to n.

# 3) Until the value i*i <= n, we will update the variable ‘ans’, with i.

# 4) Once, the value i*i becomes greater than n, we will break out from the loop as the current number i, or the numbers greater than i, cannot be our answers. 

# 5) Finally, our answer should have been stored in ‘ans’.

# CODE--

def floorSqrt(n):
    ans = 0
    # Linear search on the answer space:
    for i in range(1, n+1):
        val = i * i
        if val <= n:
            ans = i
        else:
            break
    return ans

n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)



# Output: The floor of square root of 28 is: 5

# Complexity Analysis--

# Time Complexity: O(N), N = the given number.
# Reason: Since we are using linear search, we traverse the entire answer space.

# Space Complexity: O(1) as we are not using any extra space.
