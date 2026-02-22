# A 3x3 matrix can be represented by a list of 
# nested lists: an outer list that contains three sub-lists
# that each contain three elements. 
# For example, the 3x3 matrix shown below:

'''
1  5  8
4  7  2
3  9  6

is represented by the following list of lists

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]
'''
# The transpose of a 3x3 matrix is the matrix that results 
# from exchanging the rows and columns of the original matrix.
# For example, the transposition of the matrix shown above is:
'''
1  4  3
5  7  9
8  2  6
'''

# Write a function that takes a list of lists that represents 
# a 3x3 matrix and returns the transpose of the matrix. 
# You should implement the function on your own, 
# without using any external libraries.

# Do not modify the original matrix.

# Example
# matrix = [
#     [1, 5, 8],
#     [4, 7, 2],
#     [3, 9, 6],
# ]
# --> [
# [1, 4, 3],
# [5, 7, 9], 
# [8, 2, 6]])

# DS
# Input is a list of lists
# Output will also be a list of lists

# Alg
# Let's get familiar with inputs and output locations:
# matrix[0][0] --> new_matrix [0][0]
# matrix[0][1] --> new_matrix [1][0]
# matrix[0][2] --> new_matrix [2][0]
# matrix[1][0] --> new_matrix [0][1]
# matrix[1][1] --> new_matrix [1][1]
# matrix[1][2] --> new_matrix [2][1]
# matrix[2][0] --> new_matrix [0][2]
# matrix[2][1] --> new_matrix [1][2]
# matrix[2][2] --> new_matrix [2][2]

# Based on this, we can see we need to
# build a program where the two indexes
# are reversed for building the new_matrix
# list of lists.

# def func transpose that accepts a list of lists
# Initialize an empty list
    # Append empty sublists
# iterate over the outer list using index
    # iterate over the inner list using index
        # Assign or append the values (reversing index #)
# return 


# Code
def transpose(list_of_lists):
    new_matrix_sublist_quantity = len(list_of_lists)
    new_matrix_sublist_length = len(list_of_lists[0])
    new_matrix = []
    for i in range(new_matrix_sublist_quantity):
        new_matrix.append([]) 
    for i in range(new_matrix_sublist_quantity):
        for idx in range(new_matrix_sublist_length):
            new_matrix[idx].append(list_of_lists[i][idx])
    return new_matrix 

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True
