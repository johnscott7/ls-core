# Given two lists of integers of the same length, 
# return a new list where each element is the product 
# of the corresponding elements from the two lists.

# Examples
# [1, 2, 3] and [4, 5, 6]
# --> [4, 10, 18]

# DS
# Input is two lists of ints
# Output is a list

# Alg
# Def func multiply_items
# Initialize an empty list
# Iterate over both lists using zip
    # Append each product into the new list
# Return new list

# Code
'''
def multiply_items(list_a, list_b):
    result = []
    for x, y in zip(list_a, list_b):
        result.append(x * y)
    return result
'''
# As a list comprehension
def multiply_items(list_a, list_b):
    return [x * y for x, y in zip(list_a, list_b)]


list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True