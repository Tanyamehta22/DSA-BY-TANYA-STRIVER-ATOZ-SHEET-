# METHOD---(USING SET)
# The idea of the approach is to build a Set and insert all the elements from both arrays into it. As a set stores only unique values, it will only keep all the unique values of both arrays.

# CODE--

def unionarray(arr1,arr2,n,m):
    # Create a set to store unique elements from both arrays
    set1=set(arr1)
    set2= set(arr2)
    # Merge both sets and convert back to list
    result = list(set1.union(set2))
    return result

 
# Driver code--
if __name__ == '__main__':
    arr1 = [1,2,2,2,3]
    arr2= [2,3,3,4,5,5]
    n= len(arr1)
    m= len(arr2)

    # Function call
    uni= unionarray(arr1,arr2,n,m)
    for i in uni:
        print(i, end=" ")

# Output
# 1 2 3 4 5 

# Time Complexity: O(m*log(m) + n*log(n)), where ‘m’ and ‘n’ are the size of the arrays

# Auxiliary Space: O(m + n)        