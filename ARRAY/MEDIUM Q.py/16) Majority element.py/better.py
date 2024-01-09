# METHOD-(HASHING)--
# In Hashtable(key-value pair), at value, maintain a count for each element(key), and whenever the count is greater than half of the array length, return that key(majority element). 

# STEPS--

# 1) Create a hashmap to store a key-value pair, i.e. element-frequency pair.

# 2) Traverse the array from start to end.

# 3) For every element in the array, insert the element in the hashmap if the element does not exist as a key, else fetch the value of the key ( array[i] ), and increase the value by 1

# 4) If the count is greater than half then print the majority element and break.

# 5) If no majority element is found print “No Majority element”

# CODE--

def FindMajority(arr,size):
    m={}
    for i in range(size):
        if arr[i] in m:
            m[arr[i]]+=1
        else:
            m[arr[i]]=1

    is_majority_present = False
    for key in m:
        if m[key]>size/2:
            is_majority_present=True
            print("Majority found=",key)
            break
    if not is_majority_present:
        print("No majority element")


# Driver code 
arr = [2, 2, 2, 2, 5, 5, 2, 3, 3] 
n = len(arr)
 
# Function calling 
FindMajority(arr, n)




# Output--
# Majority found = 2

# Time Complexity: O(n), One traversal of the array is needed, so the time complexity is linear.

# Auxiliary Space: O(n), Since a hashmap requires linear space.