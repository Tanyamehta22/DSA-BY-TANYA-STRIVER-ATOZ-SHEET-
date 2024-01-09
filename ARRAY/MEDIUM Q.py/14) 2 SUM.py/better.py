# METHOD--(HASHING)
# This problem can be solved efficiently by using the technique of hashing. Use a hash_map to check for the current array value x(let), if there exists a value target_sum-x which on adding to the former gives target_sum. This can be done in constant time.


# STEPS--

# 1) Initialize an empty hash table s.

# 2) Do the following for each element A[i] in A[] 

#   A) If s[x – A[i]] is set then print the pair (A[i], x – A[i])
#   B) Insert A[i] into s.


# CODE--

# function to check for the given sum
# in the array
def printPairs(arr,arr_size,sum):

    # Create an empty hash map
    # using an hashmap allows us to store the indices
    hashmap={}
    for i in range(0,arr_size):
        temp= sum-arr[i]
        if(temp in hashmap):
            print('yes')
            return
        hashmap[arr[i]]=i
    print('NO')  

# driver code
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)   


# Output--
# Yes

# Time Complexity: O(N), As the whole array is needed to be traversed only once.
# Auxiliary Space: O(N), A hash map has been used to store array elements.