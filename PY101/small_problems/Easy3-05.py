# Write a function that takes a positive integer n as an argument and prints
# a right triangle whose side each have n stars
# The hypotenuse of the triangle should have one end at the lower-left of the triangle 
# and the other end at the upper right

# Example
# triangle(5)
#     *
#    **
#   ***
#  ****
# *****

# Input will be an int passed to the function
# Output will be a bunch of printed stars

# Receive the integer
# This integer defines the number of rows
# For the first row, all the output values should be spaces, plus one star
# For the second row, all spaces, plus two stars, etc
# Last row is all stars

def triangle(n):
    for row in range(1, n + 1):
        print(' ' * (n - row) + ('*' * row))

triangle(9)