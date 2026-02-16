# Write a funcion that takes a string of digits and returns the appropriate
# number as an integer. You may not use any of the standard conversion 
# functions available in Python, such as int. Your function should
# calculate the result by using the characters in the string.

# Do not worry about leading + or - signs.
# Do not worry about invalid characters.
# Assume all characters are numeric.

# Examples
# "4321" --> 4321
# "570" --> 570

# Data structure
# input is a string
# output needs to be an integer
# intermediate data types might involve unicode, that could at least
# get me an integer

# algorithm
# convert each character in the string to its unicode value
# '0' - '9' is Unicode number 48 - 57. Therefore,
# subtract 48 from the converted value to get the original int
# Multiply the number by 10^x where x is the distance from the -1 index value
# Add all the values together

# Code
def string_to_integer(num_string):
    total_num = 0
    for char in num_string:
        total_num = (10 * total_num) + (ord(char) - ord('0'))
    return total_num


print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

