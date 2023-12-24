def insertionSortRecursive(arr,n):
    #best case
    if n<=1:
        return
    
    #sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    '''Insert last element at its correct position 
        in sorted array.'''
    last = arr[n-1]
    j=n-2

     # Move elements of arr[0..i-1], that are 
      # greater than key, to one position ahead 
      # of their current position  
    
    while(j>=0 and arr[j]>last):
        arr[j+1]=arr[j]
        j=j-1

    arr[j+1]=last

    def printArray(arr,n):
        for i in range(n):
            print(arr[i],end=" ")

    arr=[12,11,13,5,6]
    n=len(arr)
    insertionSortRecursive(arr,n)
    printArray(arr,n)    



# Output : 
# 5 6 11 12 13

# Time Complexity: O(n2)
# Auxiliary Space: O(n)    

