# METHOD--

# 1) Compare the middle element of the search space with the key. 

# 2) If the key is found at middle element, the process is terminated.

# 3) If the key is not found at middle element, choose which half will be used as the next search space.

#     A) If the key is smaller than the middle element, then the left side is used for next search.

#     B) If the key is larger than the middle element, then the right side is used for next search.

# 4) This process is continued until the key is found or the total search space is exhausted.


# CODE--

# It returns location of x in given array arr
def binarySearch(arr, l, r, x):
 
    while l <= r:
 
        mid = l + (r - l) // 2
 
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
 
        # If x is greater, ignore left half
        elif arr[mid] < x:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
 
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
 

# Output--
# Element is present at index 3

# Time Complexity: O(log N)

# Auxiliary Space: O(1)
        

# Advantages of Binary Search:--

# 1) Binary search is faster than linear search, especially for large arrays.

# 2) More efficient than other searching algorithms with a similar time complexity, such as interpolation search or exponential search.

# 3) Binary search is well-suited for searching large datasets that are stored in external memory, such as on a hard drive or in the cloud.   




# Drawbacks of Binary Search:--

# 1) The array should be sorted.

# 2) Binary search requires that the data structure being searched be stored in contiguous memory locations.

# 3) Binary search requires that the elements of the array be comparable, meaning that they must be able to be ordered.          




# Applications of Binary Search:--

# 1) Binary search can be used as a building block for more complex algorithms used in machine learning, such as algorithms for training neural networks or finding the optimal hyperparameters for a model.

# 2) It can be used for searching in computer graphics such as algorithms for ray tracing or texture mapping.

# 3) It can be used for searching a database.


