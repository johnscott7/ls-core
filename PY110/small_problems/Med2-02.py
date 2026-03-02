# A triangle is defined as:
# - All three sides have the same length (equilatoral)
# - Two sides have the same length, while the third is different (isosceles)
# - all three sides have different lengths (scalene)

# To be a valid triangle, the sum of the lengths of the two shortest sides must be 
# greater than the length of the longest side, and every side must have a length greater than 0.
# If either of these conditions is not satisfied, the triangle is invalid.

# Write a function that takes the lengths of the three sides of a triangle as 
# arguments and returns one of the following four strings representing the triangle's
# classification: 'equilateral', 'isosceles', 'scalene', or 'invalid'.

# Problem
# This is a problem determing if a triangle exists, and if so, what type
# of triangle it is, based on three length measurements (ints).
# A triangle with any side longer than its other two side, or any side <= 0,
# is invalid. 
# An equilatoral triangle is side1 = side2 = side3
# An isosceles triangle is is side1 = side2 != side 3
# A scalene triangle is side1 != side2 != side3

# Examples
# (3, 3, 3) --> "equilateral"
# 3, 4, 5 --> scalene

# Data Structure
# Input is three ints
# Output will be a string definining a triangle
# Can't immediately see a need for intermediate DS
# May be easier to do some of my calculations if the 
# three sides are in a list


# Algorithm
# def triangle to accept three int arguments
# If length of any of the sides is zero
    # return 'invalid'
# elif length of any of the sides is greater than the other two
# (Could also do if 2*any side is greater than sum of all sides)
    # return 'invalid'
    # Not sure
# elif side1 = side 2 = side 3
    # return equilateral
# elif side1 = side2, or side2 = side 3 or side 1 = side 3
    # return isosceles
# else
    # return scalene


# Code
def triangle(side1, side2, side3):
    total_length = side1 + side2 + side3
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "invalid"
    elif 2 * side1 >= total_length or 2 * side2 >= total_length or 2 * side3 >= total_length:
        return "invalid"
    elif side1 == side2 == side3:
        return "equilateral"
    elif (side1 == side2) or (side1 == side3) or (side2 == side3):
        return "isosceles"
    else:
        return "scalene"


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True