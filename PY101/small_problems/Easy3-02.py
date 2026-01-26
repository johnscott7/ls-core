# P
# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive
# duplicate characters collapsed into a single character
# E
# 'ddaaiillyy ddoouubbllee' => 'daily double'

# D
# Input will be a string
# Output will be a string

# A
# Receive a string passed as an argument
# iterating through the string, checking if the character is the same as the next (or last one)
# strings are immutable, so we cannot remove the duplicate characters
# Instead, where the char is not a duplicate, add it to a new string
# print the new string

# C
def crunch(some_string):
    new_string = ''
    prev_char = None
    for char in some_string:
        if char != prev_char:
            new_string += char
            prev_char = char
    return new_string

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')