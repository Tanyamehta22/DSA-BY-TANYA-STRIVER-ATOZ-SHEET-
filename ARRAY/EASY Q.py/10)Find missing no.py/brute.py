# METHOD 1 -- (USING HASHING)
# The numbers will be in the range (1, N), an array of size N can be maintained to keep record of the elements present in the given array.

# STEPS--

# 1) Create a temp array temp[] of size n + 1 with all initial values as 0.

# 2) Traverse the input array arr[], and do following for each arr[i]

#  A)if(temp[arr[i]] == 0) temp[arr[i]] = 1 

# 3) Traverse temp[] and output the array element having value as 0 (This is the missing element).

# CODE---

def findMissing(arr,N):

     # create a list of zeroes
    temp=[0]*(N+1)

    for i in range(0,N):
        temp[arr[i]-1]=1

    for i in range(0, N+1):
        if(temp[i]==0):
           ans=i+1  

    print(ans)

# DRIVER CODE--
if __name__=="__main__":
    arr=[1,2,3,5]
    N= len(arr)

    # Function call
    findMissing(arr,N)    

# Output--
# 4


# Time Complexity: O(N)
# Auxiliary Space: O(N)



