# Take the number 735291 and rotate it by one digit to the left,
# getting 352917. Next, keep the first digit fixed in place and
# rotate the remaining digits to get 329175. Keep the first two
# digits fixed in place and rotate again to get 321759. Keep the
# first three digits fixed in place and rotate again to get 321597.
# Finally, keep the first four digits fixed in place and rotate the
# final two digits to get 321579. The resulting number is called the
# maximum rotation of the original number.

# Write a function that takes an integer as an argument and returns
# the maximum rotation of that integer. You can (and probably should)
# use the rotate_rightmost_digits function from the previous exercise.

# Examples
# See below

# DS
# Input is an int
# Output is an int
# Int DS
    # Will need a string for sure

# Alg
# def function that accepts a number argument
# We are repeating the same process over and over in this problem
# Should iterate using a shrinking slice of the string number
# To do this, iterate over range 
# starting from the full length of the string number down to 1
#  

# Use helper function rotate_string on digits
# Separate first digit out, then use rotate_strings on rest of string

# Code

def max_rotation(number):
    length = len(str(number))
    for idx in range(length, 1, -1):
        number = rotate_rightmost_digits(number, idx)
    return number

def rotate_string(s):
    return s[1:] + s[0]

def rotate_rightmost_digits(number, count):
    str_num = str(number)
    first_chunk = str_num[:-count]
    second_chunk = str_num[-count:]
    rotated_chunk = rotate_string(second_chunk) 
    return int(first_chunk + rotated_chunk)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True