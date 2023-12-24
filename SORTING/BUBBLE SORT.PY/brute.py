# METHOD----
# In Bubble Sort algorithm--
# 1)traverse from left and compare adjacent elements and the higher one is placed at right side. 
# 2)In this way, the largest element is moved to the rightmost end at first. 
# 3)This process is then continued to find the second largest and place it and so on until the data is sorted.

# --Advantages of Bubble Sort:
# 1)Bubble sort is easy to understand and implement.
# 2)It does not require any additional memory space.
# 3)It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.

# --Disadvantages of Bubble Sort:
# 1)Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
# 2)Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set. It can limit the efficiency of the algorithm in certain cases.

def bubbleSort(arr):
    n=len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # last i element are already in place
        for j in range(0,n-i-1):

            # Traverse the array from 0 to n-i-1 
            # Sap if the element found is greater than the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                swapped = True
        if (swapped == False):
            break 


# DRIVER CODE--
if __name__ == "__main__":
    arr=[64,34,25,12,22,11,90]

    bubbleSort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" %arr[i], end=" ")


# Output---
# Sorted array: 
# 11 12 22 25 34 64 90 
        
# Complexity Analysis of Bubble Sort:
# Time Complexity: O(N2)
# Auxiliary Space: O(1)      
               