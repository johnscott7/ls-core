# This problem may prove challenging.
# Try it, but don't stress about it. If you don't solve it in 20 minutes, you can look at the answer.

# Given the following data structure, 
# write some code to return a list that contains only the dictionaries where all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

# Expected result:
# [{'e': [8], 'f': [6, 10]}]

# Could not solve this one. Solution provided below:

def list_is_even(lst):
    return all([num % 2 == 0 for num in lst])

def all_even(dictionary):
    lists_are_even = [list_is_even(list_value)
                      for list_value in dictionary.values()]
    return all(lists_are_even)

result = [dictionary for dictionary in lst
                     if all_even(dictionary)]
print(result)