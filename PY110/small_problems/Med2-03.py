# A triangle is classified as follows:

# Right: One angle is a right angle (exactly 90 degrees).
# Acute: All three angles are less than 90 degrees.
# Obtuse: One angle is greater than 90 degrees.
# To be a valid triangle, the sum of the angles must be exactly 180 degrees,
# and every angle must be greater than 0. If either of these conditions is not satisfied,
# the triangle is invalid.

# Write a function that takes the three angles of a triangle as arguments and returns one
# of the following four strings representing the triangle's
# classification: 'right', 'acute', 'obtuse', or 'invalid'.

# You may assume that all angles have integer values, so you do not have to worry about
# floating point errors. You may also assume that the arguments are in degrees.

# Problem
# This is a program to determine if a set of numbers represents a valid
# triangle and if so, what type of triangle it represents.
# A right triangle has one angle (only one) = 90 degrees.
# An acute triangle has three angles less than 90 degrees
# An obtuse triangle as one angle (only one) > 90 degrees

# Note that any triangle with a 0 degree angle or with a sum
# of angles greater than 180 degrees is not a triangle at all.

# Examples
# 60, 70, 50 --> acute
# 120, 50, 10 --> obtuse
# 0, 90, 90 --> invalid

# Data structure
# Input is three ints representing angles
# Output will be a string representing triangle type (or validity)
# Could potentially use a list, but likely not necessary

# Algorithm
# def triangle() to accept three int arguments
# if any angle less than or equal to 0
    # return "invalid"
# if sum of inputs is not equal to 180
    # return "invalid"
# if angle1 > 90 or angle2 > 90 or angle3 > 90
    # return "obtuse"
# if angle1 = 90 or angle2 = 90 or angle3 = 90
    # return "right"
# else
    # return "acute"

# Code

def triangle(angle1, angle2, angle3):
    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0:
        return "invalid"
    elif angle1 + angle2 + angle3 != 180:
        return "invalid"
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        return "obtuse"
    elif angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "right"
    else:
        return "acute"



print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True