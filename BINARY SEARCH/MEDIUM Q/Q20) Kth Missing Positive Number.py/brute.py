# METHOD--

# There might be many brute-force approaches to solve this problem. But we are going to use the following simple steps to solve the problem.

# STEPS--

# 1) We will use a loop to traverse the array.

# 2) Inside the loop,
 
#         A) If vec[i] <= k: we will simply increase the value of k by 1.

#         B) Otherwise, we will break out of the loop.

# 3) Finally, we will return the value of k.

# Note: The main idea is to shift k by 1 step if the current element is smaller or equal to k. And whenever we get a number > k, we can conclude that k is the missing number.

# CODE-

def missingK(vec, n, k):
    for i in range(n):
        if vec[i] <= k:
            k += 1  # shifting k
        else:
            break
    return k


vec = [4, 7, 9, 10]
n = 4
k = 4
ans = missingK(vec, n, k)
print("The missing number is:", ans)



# Output:The missing number is: 5.

# Complexity Analysis--

# Time Complexity: O(N), N = size of the given array.
# Reason: We are using a loop that traverses the entire given array in the worst case.

# Space Complexity: O(1) as we are not using any extra space to solve this problem.