# METHOD-

# 1) Store the string in the form of words

# 2) Run a for loop in reverse order to print the words accordingly 

# CODE-

# Python3 program to reverse a string
# s = input()
s = "i like this program very much"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)
 
 
print(" ".join(string))



# Output--
# much very program this like i

# Time Complexity: O(N)
# Auxiliary Space: O(N) 