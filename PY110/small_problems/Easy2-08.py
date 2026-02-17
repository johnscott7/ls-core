# Write a function that takes one argument, a
# positive integer, and returns a list of 
# the digits in the number.

# Example
# 12345 --> [1, 2, 3, 4, 5]

# Data
# Input is an integer
# Output is a list
# No intermediate structures needed

# Algorithm
# Initialize an empty list
# Simple for loop through the characters 
    # Append each character to the list

# Code
def digit_list(number):
    str_num = str(number)
    digits = []
    for char in str_num:
        digits.append(int(char))
    return digits

print(digit_list(12345) == [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True