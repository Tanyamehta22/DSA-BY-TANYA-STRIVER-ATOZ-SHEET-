# METHOD-3---An efficient solution is to use hashing. We create a hash table and store elements and their frequency counts as key-value pairs. Finally, we traverse the hash table and print the key with the maximum value.  

import math as mt 

def mostFrequent(arr,n):

    # INSERT AL ELEMENT IN HASH
    Hash = dict()
    for i in range(n):
        if arr[i] in Hash.keys():
            Hash[arr[i]] +=1
        else:
            Hash[arr[i]]=1


    # FIND THE MAX FREQUENCY
    max_count = 0
    res = -1
    for i in Hash:
        if (max_count < Hash[i]):
            res=i
            max_count= Hash[i]

    return res

# DRIVER CODE-
arr=[40,50,30,40,50,30,30]
n=len(arr) 
print(mostFrequent(arr,n))  


# Output-
# 30

# Time Complexity: O(n) 
# Auxiliary Space: O(n)
                                    



