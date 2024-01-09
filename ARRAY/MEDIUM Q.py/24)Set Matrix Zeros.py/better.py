# METHOD--

# In the previous approach we have updated the row and column by -1 while traversing the matrix. So Idea here is Somehow we have to store which rows and columns are supposed to mark with zeroes.

# STEPS--

# 1) A row array of size N and a col array of size M are initialized with 0 to store which row and which column to mark with zeroes.

# 2) Then, we will use two loops to traverse all the cells of the matrix.

#      A) For each cell (i, j) containing the value 0, we will mark the ith index of the row array i.e. row[i], and jth index of col array col[j] as 1. It signifies that all the elements in the ith row and jth column will be 0 in the final matrix.

# 3) Finally, we will again traverse the entire matrix and we will put 0 into all the cells (i, j) for which either row[i] or col[j] is marked as 1.

# 4) Thus we will get our final matrix.


# CODE--
def set_matrix_zeroes(matrix):
    n= len(matrix)
    m= len(matrix[0])

    # To store which rows and columns are supposed to mark with zeroes.
    row=[0]*n
    col=[0]*m

    # Traverse the matrix using nested loops
    for i in range(n):
        for j in range(m):
            # If the cell contains zero, mark its row and column as zero
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1

    for i in range(n):
        for j in range(m):
            # Set cells to zero if any of the row[i] or col[j] is 1
            if row[i] or col[j]:
                matrix[i][j] = 0
 
# Driver Code
if __name__ == "__main__":
    arr = [[0, 1, 2, 0],
           [3, 4, 5, 2],
           [1, 3, 1, 5]]
 
    # Function call
    set_matrix_zeroes(arr)    

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()        



# Output-
# 0 0 0 0 
# 0 4 5 0 
# 0 3 1 0 
        
# Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.

# Auxillary Space: O(N) + O(M), O(N) is for using the row array and O(M) is for using the col array.        