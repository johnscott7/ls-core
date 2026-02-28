# Write a function that rotates a list by
# moving the first element to the end of the list.
# Do not modify the original list;
# return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

# Examples

# [7, 3, 5, 2, 9, 1]) --> [3, 5, 2, 9, 1, 7]
# ['a', 'b', 'c']) --> ['b', 'c', 'a']
# ['a']) --> ['a']
# [1, 'a', 3, 'c']) --> ['a', 3, 'c', 1]
# [{'a': 2}, [1, 2], 3]) --> [[1, 2], 3, {'a': 2}]
# []) --> []

# return `None` if the argument is not a list
# (None) --> None
# (1) --> None

# DS
# Input is a list, but will need to be handled if not list
# Output will also be a list

# Alg
# Def func rotate_list that accepts a list argument
# check if not list
    # return None
# check if empty list
    # return empty list
# Set new_list = input list sliced from [1:]
# append input list first element to end of new_list
# return new_list


# Code
def rotate_list(input_list):
    if not isinstance(input_list, list):
        return None
    if len(input_list) == 0:
        return []
    return input_list[1:] + [input_list[0]]

print(rotate_list([7, 3, 5, 2, 9, 1]))# == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])