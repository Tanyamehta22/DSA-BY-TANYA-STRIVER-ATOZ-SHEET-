# METHOD-(COUNTING AND TRAVERSING)--
# Count the number of 0’s, 1’s and 2’s. After Counting, put all 0’s first, then 1’s and lastly 2’s in the array. We traverse the array two times. Time complexity will be O(n). 


# CODE--

import math
def sort012(arr,n):

    # Variables to maintain the count of 0's, 
    # 1's and 2's in the array
    count0=0
    count1=0
    count2=0
    for i in range(0,n):
        if(arr[i]==0):
            count0=count0+1
        if(arr[i]==1):
            count1=count1   
        if(arr[i]==2):
            count2=count2+1

    # Putting the 0's in the array in starting.
    for i in range(0,count0):
        arr[i]=0

    # Putting the 1's in the array after the 0's.    
    for i in range(count0,(count0+count1)):
        arr[i]=1

    # Putting the 2's in the array after the 1's    
    for i in range((count0+count1),n):
        arr[i]=2
    return  

# Prints the array
def printArray(arr,n):
    for i in range(0,n):
        print(arr[i], end=" ")
    print()          

# Driver code
arr = [ 0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1 ]
n = len(arr)
sort012(arr, n)
printArray(arr, n)

# Output--
# 0 0 0 0 0 1 1 1 1 1 2 2 

# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Problems with the above solution.:

# 1) It requires two traversals of array.
# 2) This solution may not work if values are a part of the structure. For example, consider a situation where 0 represents Computer Science Stream, 1 represents Electronics and 2 represents Mechanical. We have a list of student objects (or structures) and we want to sort them. We cannot use the above sort as we simply put 0s, 1s, and 2s one by one.