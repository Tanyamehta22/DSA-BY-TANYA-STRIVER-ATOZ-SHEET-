# METHOD---(USING MAP)--
# The idea of the approach is to build a Map and store the frequency of all the elements. Then insert all those elements whose frequency is greater than 0 in union array.

# CODE--

from typing import List

def Unionarray(arr1: List[int], arr2: List[int], n: int, m: int) -> List[int]:
    map = {}

    # Remove the duplicates from arr1[]
    for i in range(n):
        if arr1[i] in map:
            map[arr1[i]]+=1
        else:
            map[arr1[i]]=1 

    # Remove duplicates from arr2[]
    for i in range(m):
        if arr2[i] in map:
            map[arr2[i]] += 1
        else:
            map[arr2[i]] = 1

    # Loading set to list
    uni = list(map.keys())  
    return uni                

# Driver code
arr1 = [1, 2, 2, 2, 3]
arr2 = [2, 3, 3, 4, 5, 5]
n = len(arr1)
m = len(arr2)
print("Union is :")
 
# Function call
uni = Unionarray(arr1, arr2, n, m)
for i in uni:
    print(i, end=" ")


# Output--
# Union is :
# 1 2 3 4 5 


# Time Complexity:O(m*log(m) + n*log(n)), where ‘m’ and ‘n’ are the size of the arrays

# Auxiliary Space: O(m + n)