# Write a function that rotates the last `count`` digits of a `number``.
# To perform the rotation, move the first of the digits that you
# want to rotate to the end and shift the remaining digits to the left.


# Examples
# See below

# DS
# Input is two integers:
    # First int is 'number', second int is 'count'
# Output is an int
# Will need to convert to a string in the intermediate


# Alg
# Convert the int to a string
# Obtain two slices
    # One from start of number up to len(number) - count
    # The other, a slice of the last 'count' digits off the end
# Adjust the second slice to move the first digit to the end
# Concatenate the two slices back together
# Convert to int

# Code
'''
def rotate_rightmost_digits(number, count):
    str_num = str(number)
    first_chunk = str_num[:len(str_num) - count]
    second_chunk = str_num[-count:]
    rotated_chunk = second_chunk[1:] + second_chunk[0]
    final_str_num = first_chunk + rotated_chunk
    return int(final_str_num)
'''
# Extract to helper function
def rotate_string(s):
    return s[1:] + s[0]

def rotate_rightmost_digits(number, count):
    str_num = str(number)
    first_chunk = str_num[:-count]
    second_chunk = str_num[-count:]
    rotated_chunk = rotate_string(second_chunk)
    return int(first_chunk + rotated_chunk)
print(rotate_rightmost_digits(735291, 1))
'''
print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True
'''