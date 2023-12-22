# METHOD-2---A better solution is to do the sorting. We first sort the array, then linearly traverse the array. 

def mostFrequent(arr,n):
    
    # SORT THE ARRAY
    arr.sort()

    # FIND THE MAX FREQUENCY USING LINEAR TRAVERSAL
    max_count =1
    res=arr[0]
    curr_count=1

    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            curr_count+=1
        else:
            curr_count=1

        # IF LAST ELEMENT IS MOST FREQUENT
        if (curr_count> max_count):
            max_count=curr_count
            res=arr[i-1]

    return res

# DRIVER CODE-
arr=[40,50,30,40,50,30,30]
n=len(arr)
print(mostFrequent(arr,n))    

# Output-
# 30

# Time Complexity: O(nlog(n)) 
# Auxiliary Space: O(1)


