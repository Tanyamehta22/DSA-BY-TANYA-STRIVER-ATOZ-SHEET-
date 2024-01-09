# METHOD--
# The basic solution is to have two loops and keep track of the maximum count for all different elements. If the maximum count becomes greater than n/2 then break the loops and return the element having the maximum count. If the maximum count doesn’t become more than n/2 then the majority element doesn’t exist.

# STEPS--

# 1) Create a variable to store the max count, count = 0

# 2) Traverse through the array from start to end.

# 3) For every element in the array run another loop to find the count of similar elements in the given array.

# 4) If the count is greater than the max count update the max count and store the index in another variable.

# 5)If the maximum count is greater than half the size of the array, print the element. Else print there is no majority element.


# CODE--

# Function to find Majority
# element in an array
def FindMajority(arr,n):
    maxCount=0
    # sentinels
    index = -1
    for i in range(n):
        count=1

         # here we compare the element in 
        # ith position with i+1th position
        for j in range(i+1,n):
            if(arr[i]==arr[j]):
                count+=1
         # update maxCount if count of
        # current element is greater
        if (count > maxCount): 
            maxCount = count
            index =i

    #  if maxCount is greater than n/2
    # return the corresponding element
    if (maxCount > n//2):
        print(arr[index])  
    else:
        print("No majority element")

# Driver code
if __name__ == "__main__":
    arr = [1, 1, 2, 1, 3, 5, 1]
    n = len(arr)
 
    # Function calling
    FindMajority(arr, n)




# Output
# 1


# Time Complexity: O(n*n), A nested loop is needed where both the loops traverse the array from start to end.

# Auxiliary Space: O(1), No extra space is required.
