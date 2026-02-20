# We defined a function intending to multiply
# the sum of numbers by a factor. 
# However, the function raises an error.
# Why? How would you fix this code

'''
Buggy Code:
def sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum(numbers, 2) == 20)
'''

# Notes
# This function attempts to multiply 
# the sum of a passed in list by an int
# that is also passed into the function. 
# The function code is written corretly,
# but it is given the same name as the built-in
# Python function sum(). As a result, the custom
# function sum() is called when on numbers, when 
# the code is intended to instead call the built-in
# function sum().
# The easy solution is to rename the custom function
# to something that does not shadow a Python built-in
# function.

# Revised Code
def sum_func(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_func(numbers, 2) == 20)