# METHOD--
# By using set to remove duplicates from an input array and update the array with unique elements and finally return the count of unique elements

# STEPS--

# 1)Use set to collect unique elements from the array.

# 2)Updates the array with unique elements, modifying the size.

# 3)Prints the modified array, now containing only unique elements.
# def remove_duplicates(arr):


# CODE--
def remove_duplicates(arr):
    n=len(arr)
    if n<=1:
        return n
    
    
    # Use a set to store unique elements
    unique_elements =set(arr)

     
    # Update the original array with unique elements
    arr[:n]=unique_elements

    # Return the count of unique elements
    return len(unique_elements)

# DRIVER CODE--
if __name__ == '__main__':
    arr =[1,2,2,3,4,4,4,5,5]

    
    # Remove duplicates and get the count of unique elements
    n=remove_duplicates(arr)

    
    # Print the modified array containing unique elements
    for i in range(n):
        print(arr[i],end=" ")


# Output--
# 1 2 3 4 5 

# Time Complexity: O(N) 

# Auxiliary Space: O(N)


