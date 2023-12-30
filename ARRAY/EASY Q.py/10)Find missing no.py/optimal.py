# METHOD 3 - (USING XOR)

# XOR has certain properties -
# 1) A^A=0
# 2) A^0=A 

# STEPS--

# 1) Create two variables a = 0 and b = 0

# 2) Run a loop from i = 1 to N:
#    A)For every index, update a as a = a ^ i

# 3)Now traverse the array from i = start to end.
#    A)For every index, update b as b = b ^ arr[i].

# 4)The missing number is a ^ b.

# CODE--

def getMissingNo(a,n):
    x1=a[0]
    x2= 1

    for i in range(1,n):
        x1= x1^a[i]

    for i in range(2, n+2):
        x2=x2^i

    return x1^x2

# DRIVER CODE--
if __name__ == '__main__':
 
    arr = [1, 2, 3, 5]
    N = len(arr)
 
    # Driver code
    miss = getMissingNo(arr, N)
    print(miss)



# Output--
# 4


# Time Complexity: O(N) 
# Auxiliary Space: O(1) 


