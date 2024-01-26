# QUESTION-

# Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible for every character of str1 to every character of str2. And all occurrences of every character in ‘str1’ map to the same character in ‘str2’.

# Input:  str1 = “aab”, str2 = “xxy”
# Output: True
# Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.

# Input:  str1 = “aab”, str2 = “xyz”
# Output: False
# Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’.



# APPROACCH-

# A Simple Solution is to consider every character of ‘str1’ and check if all occurrences of it map to the same character in ‘str2’. 

# Time Complexity: O(N * N)
# Auxiliary Space: O(1)

