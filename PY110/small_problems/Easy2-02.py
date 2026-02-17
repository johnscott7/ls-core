# Write a function that takes two lists as arguments and
# returns a set that contains the union of the values
# from the two lists.
# Assume both arguments will always be lists.

# Examples
#


def union(list_x, list_y):
    return set(list_x) | set(list_y)


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True