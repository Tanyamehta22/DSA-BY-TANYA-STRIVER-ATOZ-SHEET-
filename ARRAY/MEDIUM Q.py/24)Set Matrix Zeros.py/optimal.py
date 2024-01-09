# METHOD--

# In the previous approach we had taken two arrays to store the ith row’s and jth column’s status, Idea here is to use the existing space i.e. matrix itself. We can use the first row and first column of a matrix to store which row elements and column elements to be marked as zeroes.

# STEPS-

# 1) First, we will traverse the matrix and update the first row and first column as follows we check for cell(i,j) if it is zero then we mark arr[i][0] equal to zero and arr[0][j] equal to zero.

# 2) one special case to keep in mind is when i is 0, we will mark matrix[0][0] with 0 but if j is 0, we will mark the C0 variable with 0 instead of marking matrix[0][0] again because one cell can not represent for both row and column.

# 3) Now we will traverse cells from (1,1) to (n-1,m-1) and update the matrix’s cell(i,j) according to the first row and first column.

# 4) In the end, we will change the matrix’s first row and first column of the matrix as follows, we will change the row first and then the column.

#   A) If arr[0][0] = 0, we will change all the elements from the cell (0,1) to (0, m-1), to 0.

#   B) If C0 = 0, we will change all the elements from the cell (0,0) to (n-1, 0), to 0.

# CODE--

def zeroMatrix(matrix, n, m):
    # int row[n] = {0}; --> matrix[..][0]
    # int col[m] = {0}; --> matrix[0][..]

    col0 = 1
    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark i-th row:
                matrix[i][0] = 0

                # mark j-th column:
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                # check for col & row:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    #step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix


if __name__ == "__main__":
	matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
	n = len(matrix)
	m = len(matrix[0])
	ans = zeroMatrix(matrix, n, m)

	print("The Final matrix is:")
	for row in ans:
	    for ele in row:
	        print(ele, end=" ")
            
	    


# Output: The Final matrix is: 1 0 1
#                              0 0 0
#                              1 0 1   
            


# Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
# Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

# Space Complexity: O(1) as we are not using any extra space.            