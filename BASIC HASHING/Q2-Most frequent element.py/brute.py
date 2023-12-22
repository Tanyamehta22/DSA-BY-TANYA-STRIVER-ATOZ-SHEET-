# METHOD-1---A simple solution is to run two loops. The outer loop picks all elements one by one. The inner loop finds the frequency of the picked element and compares it with the maximum so far. 

def mostFrequent(arr,n):
    maxcount=0;
    element_having_max_freq=0;
    for i in range(0,n):
        count=0
        for j in range(0,n):
            if (arr[i]==arr[j]):
                count+=1
        if(count> maxcount):
            maxcount = count
            element_having_max_freq = arr[i]

    return element_having_max_freq;

# DRIVER CODE-
arr=[40,50,30,40,50,30,30]
n=len(arr)
print(mostFrequent(arr,n))

# Output-
# 30

# The time complexity of this solution-- O(n2) since 2 loops are running from i=0 to i=n we can improve its time complexity by taking a visited  array and skipping numbers for which we already calculated the frequency.

# Auxiliary space: O(1) as it is using constant space for variables
