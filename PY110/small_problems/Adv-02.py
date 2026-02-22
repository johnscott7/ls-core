# In the previous exercise,
# you wrote a function that
# transposed a 3x3 matrix represented by a list of lists.

# Matrix transposes are not limited to 3x3 matrices, 
# or even square matrices. Any matrix can be transposed
# simply by switching columns with rows.

# Modify your transpose function from the previous exercise
# so that it works with any MxN matrix with at least one row and one column.

# DS
# Input is a list of list (any number)
# Output is an inverted list of lists

# Alg
# The previous problems code actually should
# work to handle any matrix size. I just need to 
# rename variables to make the logic more clear.

# Code
def transpose(list_of_lists):
    rows = len(list_of_lists)
    cols = len(list_of_lists[0])
    new_matrix = []
    for _ in range(cols):
        new_matrix.append([]) 
    for row in range(rows):
        for col in range(cols):
            new_matrix[col].append(list_of_lists[row][col])
    return new_matrix

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)