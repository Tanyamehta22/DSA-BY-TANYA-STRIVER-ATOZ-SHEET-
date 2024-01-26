# METHOD (USING SORTING)-

# Sort the two given strings and compare, if they are equal then they are anagram of each other.

# STEP-

# 1) Sort both strings.

# 2) Compare the sorted strings: 

#     A) If they are equal return True.
#     B) Else return False.

# CODE-

class Solution:
 
    # Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
 
        if sorted(a) == sorted(b):
            return True
        else:
            return False
 
# {
#  Driver Code Starts
 
if __name__ == '__main__':
    a = "gram"
    b = "arm"
    if(Solution().isAnagram(a, b)):
      print("The two strings are anagram of each other")
    else:
      print("The two strings are not anagram of each other")


# Output-
# The two strings are not anagram of each other

# Time Complexity: O(N * logN), For sorting.

# Auxiliary Space: O(1) as it is using constant extra space      