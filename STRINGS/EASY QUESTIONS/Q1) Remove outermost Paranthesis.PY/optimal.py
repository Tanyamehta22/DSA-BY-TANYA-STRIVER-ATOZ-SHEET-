# METHOD-

# The Optimal approach to remove the outermost parentheses from a string can be achieved using a simple algorithm that keeps track of the number of opening and closing parentheses encountered.

# STEPS-

# 1) Initialize two variables, open_count and close_count, to zero

# 2) Initialize an empty string called result.

# 3) Loop through each character c in the input string s.

# 4) If c is an opening parenthesis, increment open_count.

# 5) If c is a closing parenthesis, increment close_count.

# 6) If open_count and close_count are equal and greater than zero, this means that we have encountered a complete pair of opening and closing parentheses, so we can add the substring between them to the result string.

# 7) Reset open_count and close_count to zero.

# 8) Return the result string.


# CODE-

def remove_outer_parentheses(s):
    open_count = 0
    close_count = 0
    result = ""
    start = 0
 
    for i, c in enumerate(s):
        if c == "(":
            open_count += 1
        elif c == ")":
            close_count += 1
 
        if open_count == close_count:
            result += s[start+1:i]
            start = i+1
 
    return result
 
# Driver code
if __name__ == "__main__":
    # Example 1
    s1 = "(()())(())()"
    print(remove_outer_parentheses(s1))  
 
    # Example 2
    s2 = "()()(()())(()())"
    print(remove_outer_parentheses(s2))  
 
    # Example 3
    s3 = "((()))(())"
    print(remove_outer_parentheses(s3))


# Output-
# ()()()
# ()()()()
# (())()

# This approach has a time complexity of O(n), where n is the length of the input string s. 

# It uses constant space, except for the output string, which is proportional to the number of valid parentheses pairs in s.

