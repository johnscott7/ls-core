# From two list arguments, 
# determine the elements that are unique
# to the first list. 
# The return value should be a set.

# Examples
# [3, 6, 9, 12]
# [6, 12, 15, 18]
# --> {9, 3})

# DS
# Input is two lists
# Output is a set


# Alg
# Define a func unique_from_first that accepts two list arguments
# Convert both lists to sets
# Find the difference between the sets using difference or - and
# return the result

def unique_from_first(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 - set2

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})