# METH0D-2 USING(Using summation of first N natural numbers)--
# Find the sum of the numbers in the range [1, N] using the formula N * (N+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of the first N natural numbers. This will give the value of the missing element.

# STEPS--

# 1)Calculate the sum of the first N natural numbers as sumtotal= N*(N+1)/2.

# 2)Traverse the array from start to end.
#  A)Find the sum of all the array elements.

# 3)Print the missing number as SumTotal – sum of array

# CODE--

# Function to find the missing element
def getMissingNo(arr,n):
    total = (n+1)*(n+2)/2
    sum_of_A= sum(arr)
    return total- sum_of_A

# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
     
    #  function call
    miss = getMissingNo(arr,N)
    print(miss)


# Output--
# 4

# Time Complexity: O(N)
# Auxiliary Space: O(1)    

