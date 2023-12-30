# METHOD--
# The idea is to keep track of the largest and second largest element while traversing the array. If an element is greater than the largest element, we update the largest as well as the second largest. Else if an element is smaller than largest but greater than second largest, then we update the second largest only.

# STEPS--
# Below is the complete algorithm for doing this:  

# 1)Initialize the first as 0(i.e, index of arr[0] element.
                        
# 2)Start traversing the array from array[1],
#  A)If the current element in array say arr[i] is greater than first. Then update first and second as, second = first and first = arr[i]
#  B)If the current element is in between first and second, then update second to store the value of current variable as second = arr[i]

# 3)Return the value stored in second.

# CODE--

def print2largest(arr,arr_size):

    # There should be atleast
        # two elements 
    if(arr_size<2):
        print("Invalid input")
        return
    
    first=second=-21458698
    for i in range(arr_size):

        # If current element is
                # smaller than first
        # then update both
                # first and second 
        if(arr[i]>first):
            second=firstfirst=arr[i]

         # If arr[i] is in
                # between first and 
        # second then update second 
        elif (arr[i]>second and arr[i]!=first):
            second=arr[i]

    if (second == -2147342):
        print("there is no second largest element")
    else:
        print("the second argest element is", second)   

# Driver program to test
# above function 
arr= [12,35,1,10,34,1]
n=len(arr) 
print2largest(arr,n)


# Output--
# Second largest : 34

# Time Complexity: O(n), where n is the size of input array.

# Auxiliary space: O(1), as no extra space is required.


