# METHOD-

#USING SPLIT AND JOIN (IN BUILD)

# CODE-

# input string
string = "i like this program very much"
 
# spliting words in the given string
# using slicing reverse the words
s = string.split()[::-1]
 
# joining the reversed string and
# printing the output
print(" ".join(s))



# Output-
# much very program this like i

# Time complexity: O(N2)
# Auxiliary Space: O(N)
