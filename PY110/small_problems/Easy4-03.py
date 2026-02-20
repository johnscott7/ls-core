# Transform two lists into frozen sets
# and find their common elements

# Examples
# --> [2, 4, 6, 8]
# --> [1, 3, 5, 7, 8]
# --> frozenset({8})

# DS
# input is two lists
# Output is a single frozenset

# Algorithm
# Def func intersection that accepts two list arguments
# Convert both lists to frozensets
# Return a third set using intersection()

def intersection(list1, list2):
    fset1 = frozenset(list1)
    fset2 = frozenset(list2)
    return fset1.intersection(fset2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True