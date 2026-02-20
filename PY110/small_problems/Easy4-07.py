# Write a function that returns a list of all substrings of a string. 
# Order the returned list by where in the string the substring begins. 
# This means that all substrings that start at index position 0 should come first, 
# then all substrings that start at index position 1, and so on. 
# Since multiple substrings will occur at each position, 
# return the substrings at a given index from shortest to longest.

# Use the leading_substrings function from the previous exercise

# Example
'''
'abcde' --> [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]
'''

# DS
# Input is a string
# Output will be a list of strings

# Alg
# Def func substrings that accepts a string argument
# Intialize an empty list
# Iterate over range(len(string)) # Not len(string) + 1, since this value is start point
    # For each idx, produce a new string slice 0:len(string) + 1
        # run leading_substrings on that slice


# Code
def leading_substrings(string):
    return [string[:i] for i in range(1, len(string) + 1)]

def substrings(string):
    result = []
    for i in range(len(string)):
        result += leading_substrings(string[i:])
    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# Using a list comprehension:
def substrings_lc(string):
    return [substring for i in range(len(string)) for substring in leading_substrings(string[i:])]

print(substrings_lc('abcde') == expected_result)  # True