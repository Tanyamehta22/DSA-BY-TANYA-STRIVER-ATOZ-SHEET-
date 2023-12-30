# METHOD--
# 1) Create a local variable max and initiate it to arr[0] to store the maximum among the list

# 2) Iterate over the array
# A) Compare arr[i] with max.
# B) If arr[i] > max, update max = arr[i].
# C) Increment i once.

# 3)After the iteration is over, return max as the required answer.

# CODE---

# Function to find maximum in arr[] of size n
def largest(arr,n):

    
    # Initialize maximum element
    mx= arr[0]

    # Traverse array elements from second
    # and compare every element with
    # current max
    for i in range(1,n):
        if arr[i]>mx:
            mx=arr[i]

    return mx

# Driver Code
if __name__ == '__main__':
    arr=[10,324,45,90,9808]
    n=len(arr)

     # Calculating length of an array
    ans= largest(arr,n)

    print("largest in given array is", ans)




# Output--
# Largest in given array is 9808    
    
# Time complexity: O(N), to traverse the Array completely.

# Auxiliary Space: O(1), as only an extra variable is created, which will take O(1) space.    




    
