# METHOD (USING BITWISE OPERATORS)

# We need to check whether the last bit is 1 or not. If the last bit is 1 then the number is odd, otherwise always even.


# CODE-

def isEven(n): 
  
    # n&1 is 1, then odd, else even 
    return (not(n & 1)) 
  
  
# Driver code 
n = 101
print("Even" if isEven(n) else "Odd")



# Output-
# Odd

# Time Complexity: O(1)
# Auxiliary Space: O(1)