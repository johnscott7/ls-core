# Write a function that takes a list of positive 
# integers as input, multiplies all of the integers 
# together, divides the result by the number of entries 
# in the list, and returns the result as a string with
# the value rounded to three decimal places.

# Example
# [3, 5] --> "7.500"
# [1, 1, 1, 1] --> "0.250"

# Data 
# Input is a string
# Output is a formatted string

# Algorithm
# The problem description kind of gives an algorithm

# Intialize an int
# For loop through the list
    # Multiply int by each list element
# Divide the result by length of list
# Use f-string to give .3f (3 decimal places)

# Code
def multiplicative_average(numbers):
    product = 1
    for num in numbers:
        product *= num
    result = product / len(numbers)
    return f'{result:.3f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")