# As we saw in the previous exercises,
# a matrix can be represented by a list of lists.
# For example, the 3x3 matrix shown below is 
# represented by a list of lists:

'''
1  5  8
4  7  2
3  9  6

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
'''

# A 90-degree rotation of a matrix produces a new matrix
# in which each side of the matrix is rotated clockwise by 90 degrees.
# For example, the 90-degree rotation of the matrix shown above is:

'''
3  4  1
9  7  5
6  2  8
'''

# A 90 degree rotation of a non-square matrix is similar. 
# For example,:
'''
3  4  1
9  7  5

9  3
7  4
5  1
'''

# Write a function that takes an arbitrary MxN matrix,
# rotates it clockwise by 90-degrees as described above,
# and returns the result as a new matrix.
# The function should not mutate the original matrix.

# Examples
'''
Example1:
[
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
---> [[3, 4, 1], [9, 7, 5], [6, 2, 8]])


Example2:
[
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]
-->
[[5, 3], [1, 7], [0, 4], [8, 2]]
'''

# DS
# Input is a list of lists
# Output also a list of lists

# Algorithm
# Let's get familiar with the transformation first
# matrix --> matrix2
# length of matrix1 sublists = length of matrix2
# length of matrix1 = length of each matrix2 sublist
# matrix[0][0] --> matrix2[0][1]
# matrix[0][1] --> matrix2[1][1]
# matrix[0][2] --> matrix2[2][1]
# matrix[0][3] --> matrix2[3][1]
# matrix[1][0] --> matrix2[0][0]
# matrix[1][1] --> matrix2[1][0]
# matrix[1][2] --> matrix2[2][0]
# matrix[1][3] --> matrix2[3][0]

# So we can see that the first idx in matrix
# becomes the second idx in matrix2. The other one,
# however, is a little trickier.

# Let's look at the 3x3 matrix:
# (1) matrix[0][0] --> matrix2[0][2]
# (5) matrix[0][1] --> matrix2[1][2]
# (8) matrix[0][2] --> matrix2[2][2]
# (4) matrix[1][0] --> matrix2[0][1]
# (7) matrix[1][1] --> matrix2[1][1]
# (2) matrix[1][2] --> matrix2[2][1]
# (3) matrix[2][0] --> matrix2[0][0]
# (9) matrix[2][1] --> matrix2[1][0]
# (6) matrix[2][2] --> matrix2[2][0]

# So we can tell that the second index number for 
# each element begins at the highest index number from
# the opposite index on the initial matrix, and 
# counts down to zero from there.
# For example, len(matrix) -= i for i in range(len(matrix))

# Def function rotate90 to accept a list of lists
# define rows = len(matrix[0])
# define cols = len(matrix)
# Initialize an empty list
# Append sublists based on range(cols)
# Iterate over the rows and columns of original matrix:
# For rows in matrix:
    # for cols in matrix:
        # matrix2[col] = matrix[row][col]
        # matrix2[col][row] = len(matrix) - cols
    # return matrix

# Code
def rotate90(matrix):
    rows = len(matrix[0])   # number of columns in original
    cols = len(matrix)      # number of rows in original
    new_matrix = []

    # each column in original becomes a row in new_matrix
    for col_idx in range(rows):
        new_row = []
        for row_idx in range(cols - 1, -1, -1):
            new_row.append(matrix[row_idx][col_idx])
        new_matrix.append(new_row)

    return new_matrix

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)