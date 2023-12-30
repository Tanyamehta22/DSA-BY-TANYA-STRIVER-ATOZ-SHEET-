# METHOD-1 ---
# After rotating d positions to the left, the first d elements become the last d elements of the array

# First store the elements from index d to N-1 into the temp array.
# Then store the first d elements of the original array into the temp array.
# Copy back the elements of the temp array into the original array


# STEPS---

# 1)Initialize a temporary array(temp[n]) of length same as the original array.

# 2)Initialize an integer(k) to keep a track of the current index.

# 3)Store the elements from the position d to n-1 in the temporary array.

# 4)Now, store 0 to d-1 elements of the original array in the temporary array.

# 5)Lastly, copy back the temporary array to the original array.

# CODE---

def rotate(L,d,n):
    k=L.index(d)
    new_lis =[]
    new_lis = L[k+1:]+L[0:k+1]
    return new_lis

if __name__=='__main__':
    arr=[1,2,3,4,5,6,7]
    d=2
    N=len(arr)

     
    # Function call
    arr= rotate(arr,d,N)
    for i in arr:
        print(i,end=" ")


# Output--
# 3 4 5 6 7 1 2 

# Time complexity: O(N) 
# Auxiliary Space: O(N)
