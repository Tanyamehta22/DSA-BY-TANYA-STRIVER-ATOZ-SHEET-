# METHOD-(Dutch National Flag problem)--

# This problem is also the same as the famous “Dutch National Flag problem”. The problem was proposed by Edsger Dijkstra. The problem is as follows:

# Given N balls of colour red, white or blue arranged in a line in random order. You have to arrange all the balls such that the balls with the same colours are adjacent with the order of the balls, with the order of the colours being red, white and blue (i.e., all red coloured balls come first then the white coloured balls and then the blue coloured balls). 

# APPROACH---

# 1) The problem is similar to “Segregate 0s and 1s in an array”.

# 2) The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
#    A) arr[1] to arr[low – 1]
#    B) arr[low] to arr[mid – 1]
#    C) arr[mid] to arr[high – 1]
#    D) arr[high] to arr[n]

# 3) If the ith element is 0 then swap the element to the low range.

# 4) Similarly, if the element is 1 then keep it as it is.

# 5) If the element is 2 then swap it with an element in high range.



# STEPS--
 
# 1) Keep three indices low = 1, mid = 1, and high = N and there are four ranges, 1 to low (the range containing 0), low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).

# 2) Traverse the array from start to end and mid is less than high. (Loop counter is i)

# 3) If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1

# 4) If the element is 1 then update mid = mid + 1

# 5) If the element is 2 then swap the element with the element at index high and update high = high – 1 and update i = i – 1. As the swapped element is not processed

# 6) Print the array.



# CODE--

# Function to sort array
def sort012(a,arr_size):
    lo=0
    hi=arr_size-1
    mid=0

    # Iterate till all the elements
    # are sorted
    while mid<=hi:

        # If the element is 0
        if a[mid]==0:
            a[lo],a[mid]=a[mid],a[lo]
            lo=lo+1
            mid=mid+1

        # If the element is 1
        elif a[mid]==1:
            mid=mid+1

        # If the element is 2
        else:
            a[mid],a[hi]=a[hi],a[mid]
            hi=hi-1

    return a     

# Function to print array
def printArray(a):
    for k in a:
        print(k,end=' ')

# Driver Program
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr_size = len(arr)
arr = sort012(arr, arr_size)
printArray(arr)        



# OUTPUT--
# 0 0 0 0 0 1 1 1 1 1 2 2 

# Time Complexity: O(n), Only one traversal of the array is needed.

# Space Complexity: O(1), No extra space is required.
   
 

