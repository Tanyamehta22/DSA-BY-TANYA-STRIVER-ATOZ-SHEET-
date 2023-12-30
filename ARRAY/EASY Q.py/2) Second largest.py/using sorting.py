# METHOD--
# The idea is to sort the array in descending order and then return the second element which is not equal to the largest element from the sorted array.

# CODE--

#  Function to print the
# second largest elements--
def print2largest(arr,arr_size):
    arr.sort(reverse=True)

      # Start from second last element as first
    # element is the largest
    for i in range(1,arr_size):
           # If the element is not
        # equal to largest element
        if (arr[i]!=arr[0]):
            print("The second largest element is", arr[i])
            return
    print("there is no second largest element")

# Driver code
arr= [12,35,1,10,34,1]
n=len(arr)
print2largest(arr,n)  

# Output--
# The second largest element is 34

# Time Complexity: O(nlogn), where n is the size of input array.

# Auxiliary space: O(1), as no extra space is required.