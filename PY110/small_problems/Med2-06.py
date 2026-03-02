# Write a function that computes the difference between the square
# of the sum of the first count positive integers and the sum of the
# squares of the first count positive integers.

# Problem
# For clarity:
# The square of the sum of counted integers means sum every
# number from 1 to the int passed to the argument, thens square
# The sum of the squares of counted integers means square every number
# from 1 to (and including) the int pased to the argument, then sum.
# We need to calculate both of these, then subtract the latter from the
# former.

# Example
# 3
# Calculate (1 + 2 + 3) = 6. 6 *  6 = 36.
# Calculate 1^2 = 1, 2^2 = 4, 3^2=9. 1 + 4 + 9 = 14
# 36 - 14 = 22

# Data structure
# Input will be an integer
# Output will also be an integer, a difference of two values
# Will definitely need intermediate DS here. 
# Need a structure for the square_of_sums
# Need a structure for sum_of_squares
# Can then directly return square_of_sums - sum_of_squares
# For square_of_sums:
    # add each number to a list
    # sum the list, multiply it by itself
# for sum_of_squares:
    # Add each number in the range iteration multiplied by itself to the list
    # sum the list, return the value
# Will need four unique variables here so we are not accidentally 
# subtracting one list from the other list

# Code
# def sum_square_difference to receive an int argument 'number'
# Initiliaze square_of_sums = [] and sum_of_squares = []
# For num in range(1, number + 1)
    # append num to square_of_sums
    # append num * num to sum_of_squares
# Set Sq_of_sums_total = sum(square_of_sums) * sum(square_of_sums)
# Set Sum_of_sq_total = sum(sum_of_squares)
# return sq_of_sums_total - sum_of_sq_total


def sum_square_difference(number):
    square_of_sums = []
    sum_of_squares = []
    for num in range(1, number + 1):
        square_of_sums.append(num)
        sum_of_squares.append(num * num)
    sq_of_sum_total = sum(square_of_sums) * sum(square_of_sums)
    sum_of_sq_total = sum(sum_of_squares)
    return sq_of_sum_total - sum_of_sq_total


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True