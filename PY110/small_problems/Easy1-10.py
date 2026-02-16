# Write a function that converts a non-negative integer
# value (e.g., 0, 1, 2, 3, etc) to the string representation
# of that integer.

# Do not use standard Python conversion functions (str).

# Examples
# 4321 --> "4321"
# 0 --> "0"
# 1234567890 --> "1234567890"

# Data
# Input is an integer
# Output should be a string

# Algorithm
# Should be able to convert with chr()
# Need to reverse the math from last time

def integer_to_string(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        single_num = number % 10
        result = chr(single_num + ord('0')) + result
        number //= 10
    return result


print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True
