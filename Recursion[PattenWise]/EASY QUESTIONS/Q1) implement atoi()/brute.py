# METHOD-

# The atoi() function takes a string (which represents an integer) as an argument and returns its value. 

# APPROACH:

# The idea is to separate the last digit, recursively compute the result for the remaining n-1 digits, multiply the result by 10 and add the obtained value to the last digit. 


# CODE-

# Recursive function to compute atoi()
def myAtoiRecursive(string, num):
    # If str is NULL or str contains non-numeric
    # characters then return 0 as the number is not
    # valid
    if string.isalpha() :
         return 0;
       
    if(len(string) == 0):
         return 0;
    # base case, we've hit the end of the string,
    # we just return the last value
    if len(string) == 1:
        return int(string) + (num * 10)
         
    # add the next string item into our num value
    num = int(string[0:1]) + (num * 10)
     
    # recurse through the rest of the string
    # and add each letter to num
    return myAtoiRecursive(string[1:], num)
 
# Driver Code    
string = "112"
 
print(myAtoiRecursive(string, 0))


# Output-
# 112

# Time complexity: O(n)
# Auxiliary Space: O(n)