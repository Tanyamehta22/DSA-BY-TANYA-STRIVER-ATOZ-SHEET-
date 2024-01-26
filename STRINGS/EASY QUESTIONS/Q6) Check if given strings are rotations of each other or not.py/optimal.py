# METHOD (USING KMP ALGORITHM)-

# 1) Create a temp string and store concatenation of str1 to str1 in temp, i.e temp = str1.str1

# 2) If str2 is a substring of temp then str1 and str2 are rotations of each other.

# Example: 

# str1 = “ABACD”, str2 = “CDABA”
# temp = str1.str1 = “ABACDABACD”

# Since str2 is a substring of temp, str1 and str2 are rotations of each other.

# CODE--

# Function checks if passed strings (str1 and str2)
# are rotations of each other
 
 
def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    # string.count returns the number of occurrences of
    # the second string in temp
    if (temp.count(string2) > 0):
        return 1
    else:
        return 0
 
 
# Driver code
if __name__ == "__main__":
    string1 = "AACD"
    string2 = "ACDA"
 
    # Function call
    if areRotations(string1, string2):
        print("Strings are rotations of each other")
    else:
        print("Strings are not rotations of each other")



# Output-
# Strings are rotations of each other

# Time Complexity: O(N), where N is the length of the string.( refer from notebook)

# Auxiliary Space: O(N)