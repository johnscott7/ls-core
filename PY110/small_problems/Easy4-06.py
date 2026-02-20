# Write a function that takes a string argument
# and returns a list of substrings of that string. 
# Each substring should begin with the first letter
# of the word, and the list should be ordered from shortest to longest.

# Examples
# ('abc') --> ['a', 'ab', 'abc']
# ('a') --> ['a']
# ('xyzy') --> ['x', 'xy', 'xyz', 'xyzy']

# DS
# Input is a string
# Outpt will be a list of substrings

# Alg
# Define a function that takes a string argument
# Initialize an empty string
# Iterate over the range of values from 1 to end of list + 1
# add a slice substring from 0 to idx to the list
# sort and return the list


def leading_substrings(string):
    result = []
    for i in range(1, len(string) + 1):
        result.append(string[:i])
    return result        

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# Using a list comprehension
def leading_substrings_lc(string):
    result = []
    return [string[:i] for i in range(1, len(string) + 1)]

print(leading_substrings_lc('abc') == ['a', 'ab', 'abc'])
print(leading_substrings_lc('a') == ['a'])
print(leading_substrings_lc('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])