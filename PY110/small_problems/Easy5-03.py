# Write a function that takes a list of strings
# and returns a list of the same string values,
# but with all vowels (a, e, i, o, u) removed.

# Examples

# All of these examples should print True
# 'abcdefghijklmnopqrstuvwxyz']
# -->['bcdfghjklmnpqrstvwxyz']

# ['green', 'YELLOW', 'black', 'white']
# --> ['grn', 'YLLW', 'blck', 'wht']

# ['ABC', 'AEIOU', 'XYZ']
# --> ['BC', '', 'XYZ']

# DS
# Input is a list of strings
# Output is also a list of strings

# Alg
# Def func remove_vowels that takes a list argument
# Initialize an empty list
# Iterate over the passed in list
        # Intialize a sublist
        # Iterate over the element characters
            # For each lowercase char not in set of vowels
            # Append to sublist
        # Append sublist to empty list 
# Return list as string joined on ''

# Code
def remove_vowels(words):
    result = []
    for word in words:
        sublist = []
        for char in word:
            if char.lower() not in 'aeiou':
                sublist.append(char)
        result.append(''.join(sublist))
    return result   

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True