# Write a function that takes one argument, a positive integer, and returns the sum of its digits.

# Examples
# (23) --> 5
# (496) --> 19
# (123456789) --> 45

# DS
# Input is an int
# Output will be an int

# Alg
# Use a list comprehension

# Code
def sum_digits(num):
    str_num = str(num)
    total = 0
    for char in str_num:
        total += int(char)
    return total

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

# As a comprehension:
def sum_digits_comp(num):
    str_num = str(num)
    return sum([int(char) for char in str_num])

print(sum_digits_comp(23) == 5)              # True
print(sum_digits_comp(496) == 19)            # True
print(sum_digits_comp(123456789) == 45)      # True