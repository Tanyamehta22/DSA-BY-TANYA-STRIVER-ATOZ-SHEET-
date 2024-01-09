# METHOD--(NESTED TRAVERSAL)

# STEPS--

# 1) Traverse the array using a loop

# 2) For each element:

#   A) Check if there exists another in  the array with sum as x
#   B)Return true if yes, else continue

# 3) If no such pair is found, return false.

# CODE--

# Function to find and print pair
def chkpair(A,size,X):
    for i in range(0, size-1):
        for j in range(i+1,size):
            if(A[i]+A[j]==X):
                return 1
    return 0

# DRIVER CODE--    
if __name__ =="__main__":
    A=[0,-1,2,-3,1] 
    X=-2
    size= len(A)

    if (chkpair(A,size,X)):
        print("Yes") 
    else: 
        print("No") 


# Output--
# Yes

# Time Complexity: O(N2), Finding pair for every element in the array of size N.
# Auxiliary Space: O(1)
            