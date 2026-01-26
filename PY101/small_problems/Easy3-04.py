# Write a function that takes one argument, a positive integer, and returns a string of alternating 1s and 0s
# It should always start with a 1. The length of the string should match the given integer

# Example
# stringy(6) -> '101010'

# Input will be an integer
# Output will be a string of length integer

# Receive the integer as function argument
# Begin a loop from range 0 to int
# for each even numbered index starting with 0, output a 1
# for each odd numbered index starting wih 1, output a 0

def stringy(int):
    new_string = ''
    for i in range(0, int):
        if i % 2 == 0:
            new_string += '1'
        else:
            new_string += '0'
    return new_string

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True