# METHOD--
# One solution is to check every element if it appears once or not. Once an element with a single occurrence is found, return it. 

# CODE--

# Function to find the array 
# element that appears only once 
def find_single(A, ar_size):

     # iterate over every element 
    for i in range(ar_size):

        # Initialize count to 0
        count=0
        for j in range(ar_size):

            # Count the frequency 
            # of the element 
            if(A[i]==A[j]):
                count+=1

         # If the frequency of 
        # the element is one 
        if (count ==1):
            return A[i]        

    # If no element exist 
    # at most once 
    return -1
  
# DRIVER CODE-
ar = [2, 3, 5, 4, 5, 3, 4] 
n = len(ar) 
# Function call 
print("Element occurring once is", find_single(ar, n)) 


# Output--
# Element occurring once is 2

# Time complexity of this solution is O(n2)
# Auxiliary Space: O(1) as constant space is used.