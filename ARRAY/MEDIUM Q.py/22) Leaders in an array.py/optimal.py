# METHOD-

# The idea is to scan all the elements from right to left in an array and keep track of the maximum till now. When the maximum changes its value, print it.

# STEPS--

# 1) We start from the last index position. The last position is always a leader, as there are no elements towards its right. 

# 2) And then we iterate on the array till we reach index position = 0.

#       A) Each time we keep a check on the maximum value

#       B) Every time we encounter a maximum value than the previous maximum value encountered, we either print or store the value as it is the leader

# CODE--

def printLeaders(arr,size):

    max_from_right = arr[size-1]
    print(max_from_right, end=" ")
    for i in range(size-2,-1,-1):
        if max_from_right<arr[i]:
            print(arr[i], end=' ')
            max_from_right=arr[i]

# Driver function
arr = [16, 17, 4, 3, 5, 2]
printLeaders(arr, len(arr))            


# Output--
# 2 5 17

# Time Complexity: O(n)
# Auxiliary Space: O(1)