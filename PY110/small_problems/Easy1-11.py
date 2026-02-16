# Building on the previous exercise, write a
# function that takes an integer and converts
# it to a string representation.

# Do not use any standard Python conversion functions.
# You may use the previous exercise solution as
# a jumping off point.

# Examples
# 4321 --> "+4321"
# -123 --> "-123"
# 0 --> "0"


# Data
# Input is an integer, either positive or negative
# Output will be a string

# Algorithm
# Same as previous problem, but build in an 
# if/else block for negative numbers, then use the 
# integer_to_string function.

# Code

def integer_to_string(number):
    if number == 0:
        return '0'
    
    result = ''
    while number > 0:
        single_num = number % 10
        result = chr(single_num + ord('0')) + result
        number //= 10
    return result

def signed_integer_to_string(number):
    if number == 0:
        return '0'
    sign = '-' if number < 0 else '+'
    return sign + integer_to_string(abs(number))
    

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True