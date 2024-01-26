# TASK---

# Given a string S, representing a large integer, the task is to return the largest-valued odd integer (as a string) that is a substring of the given string S.

# Note: A substring is a contiguous sequence of characters within a string. A null string (“”) is also a substring.

# Examples:-

# Input: S = “504”
# Output: “5”
# Explanation: The only substring “5” is an odd number.


# Input: S = “2042”
# Output: “”
# Explanation: All the possible non-empty substrings have even values.


# STEPS-

# 1) Iterate through i = s.length – 1 till 0:
#     A) Check if s[i] is odd then return the substring from 0 to i+1.

# 2) Return an empty string in case of no odd number.

# CODE-

def max_odd(s):
    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
    return " "    

# Driver code
s = "504"
ans = max_odd(s)
 
# Function call
print(ans)



# Output
# 5

# Time Complexity: O(|S|).
# Auxiliary Space: O(1).

