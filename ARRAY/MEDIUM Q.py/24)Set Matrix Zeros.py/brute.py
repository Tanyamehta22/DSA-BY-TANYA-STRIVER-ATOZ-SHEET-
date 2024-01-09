# METHOD--

# 1) First, we traverse the matrix using two nested loops.

# 2) For each cell (i, j) if it is 0 then mark all the elements of row i and col j as -1 except that contains zero.

# 3) Then traverse the matrix and mark cell 0 which contains -1.

# 4) We get our final matrix.

# CODE--

def set_matrix_zeroes(matrix):
    rows ,cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols= set(), set()

    # Identify rows and columns containing zeroes
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                zero_rows.add(i)
                zero_cols.add(j)

     # Set rows with zeroes to all zeroes
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j]=0

    # Set columns with zeroes to all zeroes
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] =0


 
# Driver code
if __name__ == "__main__":
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
 
    set_matrix_zeroes(matrix)
 
    for row in matrix:
        for num in row:
            print(num, end=" ")
        print()




# Output--
# 0 0 0 0 
# 0 4 5 0 
# 0 3 1 0         

# Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix. we are traversing the matrix to find the cells with the value 0. It takes O(N*M).

# Auxillary space: O(1) as we are not using any extra space.






