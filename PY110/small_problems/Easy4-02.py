# Given two lists, convert them to sets and
# return a new set which is the union of both sets

# Examples
# [3, 5, 7, 9]
# [5, 7, 11, 13]
# --> {3, 5, 7, 9, 11, 13})

# DS
# Input is two lists
# Output is a single set

# Alg
# Def func merge_sets that receives two lists as input
# Assign each list to a new variable and convert to sets
# Merge the two using union (or |)
# return the merged set

def merge_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 | set2

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True