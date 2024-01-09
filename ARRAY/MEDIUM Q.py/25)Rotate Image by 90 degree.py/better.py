#  METHOD--

# Transform each row of original matrix into required column of final matrix. From the above picture, we can observe that:

# first row of original matrix——> last column of final matrix

# second row of original matrix——> second last column of final matrix

# so on …… last row of original matrix——> first column of final matrix


# STEPS--

# 1) Create a new matrix to hold the rotated image containing m rows and n columns.

# 2) For each element at position (i, j) in the original matrix, its new position will be(j, n - 1 - i) will be in rotated matrix ( the rows are flipped when transferring to the columns of the new matrix).

# 3) Make original matrix equal to the new matrix, which is the matrix after rotation by 90 degrees in clockwise direction.

# CODE--

# Function to rotate a N x M matrix by 90 degrees in clockwise direction
def rotateMatrix(mat):
    n = len(mat)
    m = len(mat[0])
    new_mat = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new_mat[j][n - i - 1] = mat[i][j]
    return new_mat
 
# Function to print the matrix
def displayMatrix(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()
    print()
 
# Driver code
if __name__ == "__main__":
    # Test Case 1
    mat = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]



# Output--
# 9 5 1 
# 10 6 2 
# 11 7 3 
# 12 8 4 



# Time Complexity: O(N*M), as we are using nested loops for traversing the matrix.

# Auxiliary Space: O(N*M), as we are using extra space for new matrix.





