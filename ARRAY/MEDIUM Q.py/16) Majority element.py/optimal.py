# METHOD-(MOORE VOTING ALGORITHM)

# 1) The first step gives the element that may be the majority element in the array. If there is a majority element in an array, then this step will definitely return majority element, otherwise, it will return candidate for majority element.
    
# 2) Check if the element obtained from the above step is the majority element. This step is necessary as there might be no majority element. 

# STEPS--

# 1) Loop through each element and maintains a count of the majority element, and a majority index, maj_index

# 2) If the next element is the same then increment the count if the next element is not the same then decrement the count.

# 3) if the count reaches 0 then change the maj_index to the current element and set the count again to 1.

# 4) Now again traverse through the array and find the count of the majority element found.

# 5) If the count is greater than half the size of the array, print the element

# 6) Else print that there is no majority element


# CODE --

# Function to find the candidate for Majority
def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index]== A[i]:
            count+=1
        else:
            count-=1
        if count ==0:
            maj_index=i
            count = 1
    return A[maj_index]                

# Function to check if the candidate occurs more than n/2 times
def isMajority(A,cand):
    count = 0
    for i in range(len(A)):
        if A[i]== cand:
            count+=1
    if count > len(A)/2:
        return True
    else: 
        return False
    
# Function to print Majority Element
def printMajority(A):

    # Find the candidate for Majority
    cand = findCandidate(A)
 
    # Print the candidate if it is Majority
    if isMajority(A, cand) == True:
        print(cand)
    else:
        print("No Majority Element")


# Driver code
A = [1, 3, 3, 1, 2]
 
# Function call
printMajority(A)       
     


# Output-
# No Majority Element

# Time Complexity: O(n), As two traversal of the array, is needed, so the time complexity is linear.

# Auxiliary Space: O(1), As no extra space is required.     


        
 
