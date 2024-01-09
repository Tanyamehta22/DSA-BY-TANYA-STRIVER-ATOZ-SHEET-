# METHOD--
# Naive Approach:
# The idea is to first sort the array and find the longest subarray with consecutive elements. After sorting the array and removing the multiple occurrences of elements, run a loop and keep a count and max (both initially zero). Run a loop from start to end and if the current element is not equal to the previous (element+1) then set the count to 1 else increase the count. Update max with a maximum of count and max. 


# STEPS--

# 1) Initialize ans and countConsecutive with 0.

# 2) Sort the arr[].

# 3) Store the distinct elements in dist[] array by traversing over the arr[].

# 4) Now, traverse on the dist[] array to find the count of consecutive elements.

# 5) Simultaneously maintain the answer variable.

# CODE--

# Python3 program to find longest
# contiguous subsequence
 
# Returns length of the longest
# contiguous subsequence

def findLongestConseqSubseq(arr,n):
    ans= 0
    count=0

    # Sort the array
    arr.sort()

    v=[]

    v.append(arr[0])

    # Insert repeated elements only
    # once in the vector
    for i in range(1,n):
        if (arr[i]!= arr[i-1]):
            v.append(arr[i])

    # Find the maximum length
    # by traversing the array        
    for i in range(len(v)):

        # Check if the current element is
        # equal to previous element +1
        if(i>0 and v[i]==v[i-1] + 1):
            count+=1

        # Reset the count
        else:
            count = 1

        # Update the maximum
        ans = max(ans,count)       
        
    return ans  

# Driver code
arr = [1, 2, 2, 3]
n = len(arr)
 
print("Length of the Longest contiguous subsequence is",
      findLongestConseqSubseq(arr, n)) 




# Output--
# Length of the Longest contiguous subsequence is 3


# Time complexity: O(Nlog(N)), Time to sort the array is O(Nlog(N)).

# Auxiliary space: O(N). Extra space is needed for storing distinct elements.


