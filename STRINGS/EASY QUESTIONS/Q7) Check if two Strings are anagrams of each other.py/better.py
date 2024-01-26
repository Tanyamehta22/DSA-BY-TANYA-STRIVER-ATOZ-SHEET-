# METHOD(BY COUNTING FREQUENCY)--

# The idea is based in an assumption that the set of possible characters in both strings is small. that the characters are stored using 8 bit and there can be 256 possible characters. 

# So count the frequency of the characters and if the frequency of characters in both strings are the same, they are anagram of each other.

# STEPS-

# 1) Create count arrays of size 256 for both strings. Initialize all values in count arrays as 0.

# 2) Iterate through every character of both strings and increment the count of characters in the corresponding count arrays.

# 3) Compare count arrays. If both count arrays are the same, then return true else return false.

# CODE--

NO_OF_CHARS = 256
 
# Function to check whether two strings are anagram of
# each other
 
 
def areAnagram(str1, str2):
 
    # Create two count arrays and initialize all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
 
    # For each character in input strings, increment count
    # in the corresponding count array
    for i in str1:
        count1[ord(i)] += 1
 
    for i in str2:
        count2[ord(i)] += 1
 
    # If both strings are of different length. Removing this
    # condition will make the program fail for strings like
    # "aaca" and "aca"
    if len(str1) != len(str2):
        return 0
 
    # Compare count arrays
    for i in xrange(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0
 
    return 1
 
 
# Driver code
str1 = "gram"
str2 = "arm"
 
# Function call
if areAnagram(str1, str2):
    print 'The two strings are anagram of each other'
else:
    print "The two strings are not anagram of each other"



# Output-
# The two strings are not anagram of each other

# Time Complexity: O(n)

# Auxiliary Space: O(256) i.e. O(1) for constant space.