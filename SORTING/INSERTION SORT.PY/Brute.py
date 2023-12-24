# METHOD--
# Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

# ALGORITHM--
# To sort an array of size N in ascending order iterate over the array and compare the current element (key) to its predecessor, if the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

# Characteristics of Insertion Sort--
# This algorithm is one of the simplest algorithms with a simple implementation
# Basically, Insertion sort is efficient for small data values
# Insertion sort is adaptive in nature, i.e. it is appropriate for data sets that are already partially sorted.

# CODE-
def insertionSort(arr):

    # TRAVERSE THROUGH 1 TO LEN(ARR)
    for i in range(1,len(arr)):
        key=arr[i]
        
        # MOVE ELEMENTS OF ARR[0..i-1], THAT ARE GREATER THAN KEY, TO ONE POSITION AHEAD OF THEIR CURRENT POSITION
        j= i-1
        while j >=0 and key<arr[j]:
            a[j+1]= arr[j]
            j-=1
        arr[j+1]=key

# DRIVER CODE-
arr=[12,11,13,5,6]
insertionSort(arr)
for i in range(len(arr)):
    print("%d" % arr[i])


# Output--
# 5 6 11 12 13 

# Time Complexity: O(N^2) 

# Time Complexity of Insertion Sort---
# The worst-case time complexity of the Insertion sort is O(N^2)
# The average case time complexity of the Insertion sort is O(N^2)
# The time complexity of the best case is O(N).


# Auxiliary Space: O(1)    

