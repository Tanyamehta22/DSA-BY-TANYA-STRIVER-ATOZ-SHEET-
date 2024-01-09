# METHOD--

# In this approach, we will be using four loops to print all four sides of the matrix.

# 1st loop: This will print the elements from left to right.

# 2nd loop: This will print the elements from top to bottom.

# 3rd loop: This will print the elements from right to left.

# 4th loop: This will print the elements from bottom to top.

# STEPS--

# 1) Create and initialize variables top as starting row index, bottom as ending row index left as starting column index, and right as ending column index.

# 2) In each outer loop traversal print the elements of a square in a clockwise manner.

# 3) Print the top row, i.e. Print the elements of the top row from column index left to right and increase the count of the top so that it will move to the next row.

# 4) Print the right column, i.e. Print the rightmost column from row index top to bottom and decrease the count of right.

# 5) Print the bottom row, i.e. if top <= bottom, then print the elements of a bottom row from column right to left and decrease the count of bottom

# 6) Print the left column, i.e. if left <= right, then print the elements of the left column from the bottom row to the top row and increase the count of left.

# 7) Run a loop until all the squares of loops are printed.


# CODE--

def printSpiral(mat):
    # Define ans array to store the result.
    ans = []
 
    n = len(mat) # no. of rows
    m = len(mat[0]) # no. of columns
  
    # Initialize the pointers reqd for traversal.
    top = 0
    left = 0
    bottom = n - 1
    right = m - 1

    # Loop until all elements are not traversed.
    while (top <= bottom and left <= right):
        # For moving left to right
        for i in range(left, right + 1):
            ans.append(mat[top][i])

        top += 1

        # For moving top to bottom.
        for i in range(top, bottom + 1):
            ans.append(mat[i][right])

        right -= 1

        # For moving right to left.
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                ans.append(mat[bottom][i])

            bottom -= 1

        # For moving bottom to top.
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                ans.append(mat[i][left])

            left += 1

    return ans

#Matrix initialization.
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]
                     
ans = printSpiral(mat)

print(ans)




# Output:

# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

# Time Complexity: O(m x n) { Since all the elements are being traversed once and there are total n x m elements ( m elements in each row and total n rows) so the time complexity will be O(n x m)}.

# Space Complexity: O(n) { Extra Space used for storing traversal in the ans array }.