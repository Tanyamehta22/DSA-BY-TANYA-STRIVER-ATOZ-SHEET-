# METHOD--Most of the languages have a relevant max() type in-built function to find the maximum element, such as  std::max_element in C++. We can use this function to directly find the maximum element.  

# CODE--

# Returns maximum in arr[] of size n
def largest(arr,n):
    return max(arr)

# Driver code
if __name__=='__main__':
    arr=[10,324,45,90,9808]
    n=len(arr)

    # Function call
    print(largest(arr, n))



# Output--
# 9808

# Time complexity: O(N), since the in-built max_element() function takes O(N) time.

# Auxiliary Space: O(1), as only an extra variable is created, which will take O(1) space.
 