# METHOD ( CHARACTER BY CHARACTER)-

# Input  : {“geeksforgeeks”, “geeks”, “geek”, “geezer”}
# Output : "gee"

# Input  : {"apple", "ape", "april"}
# Output : "ap"

# We have discussed word by word matching algorithm in previous post.
# In this algorithm, instead of going through the strings one by one, we will go through the characters one by one. 

# CODE-

# A Function to find the string having the minimum
# length and returns that length
def findMinLength(arr, n):
 
    min = len(arr[0])
  
    for i in range(1,n):
        if (len(arr[i])< min):
            min = len(arr[i])
  
    return(min)
  
# A Function that returns the longest common prefix
# from the array of strings
def commonPrefix(arr, n):
 
    minlen = findMinLength(arr, n)
    result =""
    for i in range(minlen):
     
        # Current character (must be same
        # in all strings to be a part of
        # result)
        current = arr[0][i]
  
        for j in range(1,n):
            if (arr[j][i] != current):
                return result
  
        # Append to result
        result = result+current
  
    return (result)
  
# Driver program to test above function
if __name__ == "__main__":
     
    arr = ["geeksforgeeks", "geeks",
                    "geek", "geezer"]
    n = len(arr)
  
    ans = commonPrefix (arr, n)
  
    if (len(ans)):
        print("The longest common prefix is ",ans)
    else:
        print("There is no common prefix")



# Output-
# The longest common prefix is gee   

# Time Complexity : Since we are iterating through all the characters of all the strings, so we can say that the time complexity is O(N M) where, 

# N = Number of strings
# M = Length of the Smallest string 

# Auxiliary Space : To store the longest prefix string we are allocating space which is O(M).
