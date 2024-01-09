# METHOD-

# Following are the steps of this approach:

# 1) Transposition: The transposed_image matrix is created by swapping the rows and columns of the input image. This is achieved by iterating over the rows and columns of the input image and creates a new matrix where the rows and columns are swapped.

# 2) Reverse Rows: The rotated_image matrix is created by reversing the order of rows in the transposed_image matrix. This step effectively rotates the image by 90 degrees clockwise.

# 3) Finally, the rotated image is printed by iterating over the rows of rotated_image matrix and printing them.

# CODE--

from typing import List
def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()




if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()



# Output:

# Rotated Image
# 7 4 1
# 8 5 2
# 9 6 3

# Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.

# Space Complexity: O(1).

