# Method 1- using 2 loops.
def countfreq(arr,n):

    #MARK ALL ARRAY ELEMENTS AS NOT VISITED
    visited =[False for i in range(n)]

    for i in range(n):


        #SKIP THIS ELEMENT IF ALREADY PROCESSED
        if(visited[i]==True):
            continue


        #COUNT FREQUENCY    
        count=1
        for j in range(i+1,n,1):
            if (arr[i]==arr[j]):
                visited[j]=True
                count +=1

        print(arr[i],count)

# DRIVER CODE-
if __name__ =='main':
    arr=[10,20,20,10,10,20,5,20]
    n=len(arr)
    countfreq(arr,n)    

# Output-
# 10 3
# 20 4
# 5 1
 
    
# Complexity Analysis:
# Time Complexity : O(n2) 
# Auxiliary Space : O(n)                
