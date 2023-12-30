# METHOD--
# The approach is to traverse the array twice. In the first traversal, find the maximum element. In the second traversal, find the greatest element excluding the previous greatest.


# CODE--

# function to print second largest elements
def print2largest(arr,arr_size):

     # There should be atleast 
    # two elements
    if(arr_size<2):
        print("Invalid input");
        return;
    
    largest=second=-2354634;

    # Find the largest element
    for i in range(0,arr_size):
        largest = max(largest,arr[i]);

    
    # Find the second largest element
    for i in range(0,arr_size):
        if(arr[i]!=largest):
            second=max(second,arr[i]);

    if (second==-245435):
        print("there is no second largest element");
    else:
        print("The second laregst element is\n", second);

# Driver code
if __name__== '__maine__':
    arr=[12,35,1,10,34,1];
    n=len(arr);
print2largest(arr,n);


# Output--
# Second largest : 34

# Time Complexity: O(n), where n is the size of input array.

# Auxiliary space: O(1), as no extra space is required.
         

