# METHOD-

# Comparing the prefix and suffix

# STEPS-

# 1) Check if sizes of two strings are not same, then return false.

# 2) Check if ith character is equal to the first character of str2

#     A) Check prefix of str1 with suffix of str2

#     B) Check suffix of str2 with prefix of str1

# 3) If none of the above cases satisfy then answer must be false so, return false

# CODE-

# Function checks if passed strings (s1 and s2)
# are rotations of each other
 
 
def areRotations(s1, s2):
    # check length of both strings are equal or not
    if len(s1) != len(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i] == s2[0]:  # compare the ith charcter in s1 with first character of s2
                if s1[i:] == s2[:len(s1)-i]:  # compare prefix of s2 with suffix of s1
                    # compare prefix of s1 with suffix of s2
                    if s1[:i] == s2[len(s1)-i:]:
                        return True
    return False
 
 
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

# Time Complexity: O(N*N), where N is the length of the string and another N because we compare two string.

# Auxiliary Space: O(N) , Because we are creating substring

