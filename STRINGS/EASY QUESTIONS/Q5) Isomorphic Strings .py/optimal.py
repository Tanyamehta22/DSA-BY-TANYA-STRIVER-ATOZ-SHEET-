# METHOD-(USING MAPPING-SINGLE)
 
# The idea is to store map the character and check whether the mapping is correct or not

# STEPS-

# 1) Create a hashmap of (char, char) to store the mapping of str1 and str2.

# 2) Now traverse on the string and check whether the current character is present in the Hashmap.

#         A) If it is present then the character that is mapped is there at the ith index or not.

#         B) Else check if str2[i] is not present in the key then add the new mapping.

# 3) Else return false.
 


# CODE--

def isisomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        map1, map2 = {}, {}
        for i in range(len(str1)):
            ch1, ch2 = str1[i], str2[i]
            if ch1 not in map1:
                map1[ch1] = ch2
            if ch2 not in map2:
                map2[ch2] = ch1
            if map1[ch1] != ch2 or map2[ch2] != ch1:
                return False
    return True


str1 = "abacba"
str2 = "xpxcpx"
print(isisomorphic(str1, str2))
 


# Output-
# True

# Time Complexity: O(N), traversing over the string of size N.
# Auxiliary Space: O(1) 

