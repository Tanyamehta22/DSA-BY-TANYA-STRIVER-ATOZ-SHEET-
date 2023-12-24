# METHOD--
# Merge sort is a recursive algorithm that continuously splits the array in half until it cannot be further divided i.e., the array has only one element left (an array with one element is always sorted). Then the sorted subarrays are merged into one sorted array.

# Applications of Merge Sort:--
# 1)Sorting large datasets: Merge sort is particularly well-suited for sorting large datasets due to its guaranteed worst-case time complexity of O(n log n).
# 2)External sorting: Merge sort is commonly used in external sorting, where the data to be sorted is too large to fit into memory.
# 3)Custom sorting: Merge sort can be adapted to handle different input distributions, such as partially sorted, nearly sorted, or completely unsorted data.
# 4)Inversion Count Problem


# Advantages of Merge Sort:---
# 1)Stability: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal elements in the input array.
# 2)Guaranteed worst-case performance: Merge sort has a worst-case time complexity of O(N logN), which means it performs well even on large datasets.
# 3)Parallelizable: Merge sort is a naturally parallelizable algorithm, which means it can be easily parallelized to take advantage of multiple processors or threads.


# Drawbacks of Merge Sort:
# 1)Space complexity: Merge sort requires additional memory to store the merged sub-arrays during the sorting process. 
# 2)Not in-place: Merge sort is not an in-place sorting algorithm, which means it requires additional memory to store the sorted data. This can be a disadvantage in applications where memory usage is a concern.
# 3)Not always optimal for small datasets: For small datasets, Merge sort has a higher time complexity than some other sorting algorithms, such as insertion sort. This can result in slower performance for very small datasets.


# CODE--

def mergeSort(arr):
    if len(arr)>1:

        # FINDING THE MID OF THE ARRAY
        mid= len(arr)//2

        # DIVIDING THE ARRAY ELEMENTS INTO 2 HALVES
        L=arr[:mid]

        R= arr[mid:]

        # SORTING THE FIRST HALF
        mergeSort(L)

        # SORTING THE SECOND HALF
        mergeSort(R)

        i=j=k=0

        # COPY DATA TO TEMP ARRAYS L[] AND R[]
        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        # CHECKING IF ANY ELEMENT WAS LEFT 
        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1 

# CODE TO PRINT THE LIST--
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ") 
    print()

# DRIVER CODE-
if __name__ == '__maine__':
    arr=[12,11,13,5,6,7]
    print("given array is")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is")
    printList(arr)

# Output---
# Given array is 
# 12 11 13 5 6 7 
# Sorted array is 
# 5 6 7 11 12 13  


# Complexity Analysis of Merge Sort----

# Time Complexity: O(N log(N)),  Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 

# T(n) = 2T(n/2) + θ(n)

# The above recurrence can be solved either using the Recurrence Tree method or the Master method. It falls in case II of the Master Method and the solution of the recurrence is θ(Nlog(N)). The time complexity of Merge Sort isθ(Nlog(N)) in all 3 cases (worst, average, and best) as merge sort always divides the array into two halves and takes linear time to merge two halves.
                     

# Auxiliary Space: O(N), In merge sort all elements are copied into an auxiliary array. So N auxiliary space is required for merge sort.                     




