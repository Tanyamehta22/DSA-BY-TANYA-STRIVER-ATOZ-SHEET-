# METHOD-- (HASHING)

# We can simply use a hashmap to store the frequency of the elements and after that we can iterate the hashmap to find the element with frequency 1.
    
# STEPS--

# 1) Traverse all elements and put them in a hash table. Element is used as key and the count of occurrences is used as the value in the hash table.

# 2) Traverse the array again and print the element with count 1 in the hash table.

# CODE----
def singlelement(arr,n):
    #dictionary to store frequency 
    mm={}
    for i in range(n):
        #storing frequency 
        if arr[i] in mm:
            mm[arr[i]]+=1
        else:
            mm[arr[i]]=1

    #iterating over dictionary
    for key,value in mm.items():
        #returning element with frequency 1 
        if value ==1:
            return key
        
#Driver code 
arr = [2, 3, 5, 4, 5, 3, 4] 
size = len(arr) 
arr.sort() 
print(singlelement(arr, size))         


# Output---
# 2

# Time Complexity:- O(N)
# Auxiliary Space:- O(N)
