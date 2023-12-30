# METHOD---
# Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise the search continues till the end of the data set. 

# STEPS--

# In Linear Search Algorithm, 

# 1) Every element is considered as a potential match for the key and checked for the same.

# 2) If any element is found equal to the key, the search is successful and the index of that element is returned.

# 3) If no element is found equal to the key, the search yields “No match found”.

# CODE--

def search(arr,N,x):
    for i in range(0,N):
        if (arr[i]==x):
            return i
    return -1

# Driver Code 
if __name__=="__main__":
    arr=[2,3,4,10,40]
    x=10
    N=len(arr)

    result=search(arr,N,x)
    if(result==-1):
        print("element is not present in array")
    else:
        print('Element is present at index', result)

# Output--
# Element is present at index 3


# Complexity Analysis of Linear Search:

# Time Complexity:

# 1) Best Case: In the best case, the key might be present at the first index. So the best case complexity is O(1)

# 2) Worst Case: In the worst case, the key might be present at the last index i.e., opposite to the end from which the search has started in the list. So the worst-case complexity is O(N) where N is the size of the list.

# 3) Average Case: O(N)

# Auxiliary Space: O(1) as except for the variable to iterate through the list, no other variable is used.     
        

# Advantages of Linear Search:

# 1) Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays of any data type.
# 2) Does not require any additional memory.

# 3) It is a well-suited algorithm for small datasets.

# Drawbacks of Linear Search:

# 1) Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
# 2) Not suitable for large arrays.
    
# When to use Linear Search?

# 1) When we are dealing with a small dataset.

# 2) When you are searching for a dataset stored in contiguous memory.



