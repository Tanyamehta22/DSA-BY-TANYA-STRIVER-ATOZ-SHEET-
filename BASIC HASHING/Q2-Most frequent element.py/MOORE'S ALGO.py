# METHOD-4 --An efficient solution to this problem can be to solve this problem by Moore’s voting Algorithm.

# NOTE: THE ABOVE VOTING ALGORITHM ONLY WORKS WHEN THE MAXIMUM OCCURRING ELEMENT IS MORE THAN (SIZEOFARRAY/2) TIMES;

# In this method, we will find the maximum occurred integer by counting the votes a number has.


def maxFreq(arr,n):

    # USING MOORE'S VOTING ALGORITHM
    res=0
    count = 1

    for i in range(1,n):
        if (arr[i]== arr[res]):
            count +=1
        else:
            count -=1

        if (count==0):
            res=i  
            count =1

    return arr[res]

# DRIVER CODE--
arr= [40,50,30,40,50,30,30]
n=len(arr)
freq= maxFreq(arr,n)
count =0

for i in range(arr,n):
    if(arr[i]==freq):
        count +=1

print ("Element", maxFreq(arr,n),
       "occur", count, 'times') 


# Output--
# Element 30 occurs 3 times

# Time Complexity: O(n)
# Auxiliary Space: O(1)




