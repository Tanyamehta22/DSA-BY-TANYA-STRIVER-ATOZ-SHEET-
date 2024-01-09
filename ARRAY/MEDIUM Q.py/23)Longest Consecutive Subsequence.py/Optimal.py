# METHOD (HASHING)-

# The idea is to use Hashing. We first insert all elements in a Set. Then check all the possible starts of consecutive subsequences.

# STEPS--

# 1) Create an empty hash.

# 2) Insert all array elements to hash.
# Do the following for every element arr[i]
    
# 3) Check if this element is the starting point of a subsequence. To check this, simply look for arr[i] – 1 in the hash, if not found, then this is the first element of a subsequence.

# 4) If this element is the first element, then count the number of elements in the consecutive starting with this element. Iterate from arr[i] + 1 till the last element that can be found.

# 5) If the count is more than the previous longest subsequence found, then update this.

# CODE--

def findLongestConseqSubseq(arr,n):
    s=set()
    ans=0

    # Hash all the array elements
    for ele in arr:
        s.add(ele)

    # check each possible sequence from the start
    # then update optimal length
    for i in range(n):

        # if current element is the starting
        # element of a sequence
        if (arr[i]-1) not in s:

            # Then check for next elements in the
            # sequence
            j=arr[i]
            while(j in s):
                j+=1

            # update  optimal length if this length
            # is more
            ans=max(ans,j-arr[i])
    return ans            

# Driver code
if __name__ == '__main__':
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print("Length of the Longest contiguous subsequence is ",
          findLongestConseqSubseq(arr, n))
    



# Output-
# Length of the Longest contiguous subsequence is 4

# Time complexity: O(N), Only one traversal is needed and the time complexity is O(n) under the assumption that hash insert and search takes O(1) time.

# Auxiliary space: O(N), To store every element in the hashmap O(n) space is needed.







 


