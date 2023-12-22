# METHOD 3- USING BINARY SEARCH FUNCTION--

from bisect import bisect_left,bisect_right

# FUNCTION TO FIND FREQUENCY OF ELEMENTS IN THE ARRAY
def countfreq(arr,n):
    # SORT ARRAY FOR BINARY SEARCH
    arr.sort() 


    i=0
    while i<n:
        # INDEX OF FIRST AND LAST OCC OF ARR[i]
        first_index = bisect_left(arr,arr[i])
        last_index=bisect_right(arr,arr[i])-1
        i=last_index+1


        # FINDING FREQUENCY
        freq=last_index-first_index+1 
        # PRINTING FREQUENCY
        print(arr[i-1],freq) 



# DRIVER CODE-
arr=[10,20,20,10,10,20,5,20]
n=len(arr)
countfreq(arr,n)    


# Output-
# 5 1
# 10 3
# 20 4


# Time Complexity: O(n*log2n) , where O(log2n) time for binary search function .
# Auxiliary Space: O(1)  