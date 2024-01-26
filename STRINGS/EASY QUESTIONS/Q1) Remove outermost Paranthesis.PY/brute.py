# METHOD-

# A valid parentheses substring S is primitive if it is non-empty, and cannot be split into two or more non-empty substrings which are also a valid parentheses.

# STEPS-

# 1) Initialize a variable count to store the number of opening parentheses, i.e. ‘(‘.

# 2) Add every ‘(‘ to the result if count is greater than 0, i.e. add all ‘(‘ after the first ‘(‘ of a primitive substring is encountered.

# 3) Add every ‘)’ to the result if count is greater than 1, i.e. add all ‘)’ before the last ‘)’ of a primitive substring is encountered.

# 4) Finally, print the resultant string obtained.


# CODE--

# Function to remove the outermost
# parentheses of every primitive
# substring from the given string
def removeOuterParentheses(S):
     
    # Stores the resultant string
    res = ""
 
    # Stores the count of
    # opened parentheses
    count = 0
 
    # Traverse the string
    for c in S:
         
        # If opening parentheses is
        # encountered and their
        # count exceeds 0
        if (c == '(' and count > 0):
 
            # Include the character
            res += c

        if (c == '('):
            count += 1
            
        # If closing parentheses is
        # encountered and their
        # count is less than count
        # of opening parentheses
        
        if (c == ')' and count > 1):
 
            # Include the character
            res += c
             
        if (c == ')'):
          count -= 1
     
    # Return the resultant string
    return res
 
# Driver Code
if __name__ == '__main__':
     
    S = "(()())(())()"
     
    print(removeOuterParentheses(S))



# Output-
# ()()()

# Time Complexity: O(N) where n is number of elements in given string. As, we are using a loop to traverse N times so it will cost us O(N) time 

# Auxiliary Space: O(N), as we are using extra space for string.    
