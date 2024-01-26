# METHOD- Without splitting the string

# By this approach, we can even remove extra trailing spaces and in between the words also.

# Basically, this algorithm involves 3 steps.

# If you find white space, there can be two possibilities. 
# It might be end of a word or else extra trailing space in between the words.
# if it is not a white space, add the character to temporary word as shown in the below code.

# CODE--

def reverseString(s):
    ans = ""
    temp = ""
    for ch in s:
        if ch == ' ':
            if temp:
                ans = temp + " " + ans
            temp = ""
        else:
            temp += ch
 
    if temp:
        ans = temp + " " + ans
 
    if ans and ans[-1] == ' ':
        ans = ans[:-1]
 
    return ans
 
if __name__ == "__main__":
    s1 = " Welcome to Geeks For Geeks "
    print("Before reversing length of string:", len(s1))
    ans1 = reverseString(s1)
    print("After reversing length of string:", len(ans1))
    print("\"" + ans1 + "\"")
 
    s2 = " I Love Python Programming     "
    print("Before reversing length of string:", len(s2))
    ans2 = reverseString(s2)
    print("After reversing length of string:", len(ans2))
    print("\"" + ans2 + "\"")



# Output--

# Before reversing length of string : 28
# After reversing length of string : 26
# "Geeks For Geeks to Welcome"

# Before reversing length of string : 31
# After reversing length of string : 23
# "Programming Java Love I"

# Time Complexity: O(N) where N is length of string

# Auxiliary Space: O(1) 