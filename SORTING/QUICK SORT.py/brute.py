# METHOD--
# --QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

# --The logic is simple, we start from the leftmost element and keep track of the index of smaller (or equal) elements as i. While traversing, if we find a smaller element, we swap the current element with arr[i]. Otherwise, we ignore the current element.


# Advantages of Quick Sort:
# 1) It is a divide-and-conquer algorithm that makes it easier to solve problems.
# 2) It is efficient on large data sets.
# 3) It has a low overhead, as it only requires a small amount of memory to function.


# Disadvantages of Quick Sort:
# 1) It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.
# 2) It is not a good choice for small data sets.
# 3) It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved in the sorted output in case of quick sort, because here we are swapping elements according to the pivot’s position (without considering their original positions).

# CODE---

# Function to find the partition position
def partition(array,low,high):

    # Choose the rightmost element as pivot
    pivot = array[high]

    # Pointer for greater element
    i=low-1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low,high):
        if array[j]<=pivot:
            
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i=i+1

            # Swapping element at i with element at j
            (array[i], array[j])= (array[j],array[i])

    # Swap the pivot element with
    # the greater element specified by i 
    (array[i+1],array[high]) = (array[high], array[i+1])


    # Return the position from where partition is done  
    return i + 1 

# Function to perform quicksort
def quicksort(array,low,high):
    if low<high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi= partition(array,low,high)

        # Recursive call on the left of pivot
        quicksort(array,low,pi-1)

        # Recursive call on the right of pivot
        quicksort(array,pi+1,high)  

# DRIVER CODE--
if __name__ == '__main__':
    array=[10,7,8,9,1,5]
    N=len(array)

    # Function call
    quicksort(array,0,N-1)
    print('sorted array:')
    for x in array:
        print(x,end=" ")


# Output---
# Sorted array: 
# 1 5 7 8 9 10 
        

# Time Complexity:

# 1)Best Case: Ω (N log (N))
# The best-case scenario for quicksort occur when the pivot chosen at the each step divides the array into roughly equal halves.
# In this case, the algorithm will make balanced partitions, leading to efficient Sorting.

# 2)Average Case: θ ( N log (N))
# Quicksort’s average-case performance is usually very good in practice, making it one of the fastest sorting Algorithm.  

# 3) Worst Case: O(N2)
# The worst-case Scenario for Quicksort occur when the pivot at each step consistently results in highly unbalanced partitions. When the array is already sorted and the pivot is always chosen as the smallest or largest element. To mitigate the worst-case Scenario, various techniques are used such as choosing a good pivot (e.g., median of three) and using Randomized algorithm (Randomized Quicksort ) to shuffle the element before sorting.
    

# --Auxiliary Space: O(1), if we don’t consider the recursive stack space. If we consider the recursive stack space then, in the worst case quicksort could make O(N).    