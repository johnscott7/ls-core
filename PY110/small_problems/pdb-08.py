# We have a list of lists and want to
# duplicate it. After making the copy,
# we modify the original list, but the 
# copied list also seems to be affected:

'''Buggy code:
import copy

original = [[1], [2], [3]]
copied = copy.copy(original)

original[0][0] = 99

print(copied[0] == [1])
'''
# What's wrong here? How can you fix it?

# Notes
# Copies in Python are shallow copies by 
# default, which means the nested lists
# refer to the same list objects, which is why
# the copied list sees changes to their nested
# lists as well. 

# The solution is to create a deepcopy, which
# results in the nested lists being copies
# as well, and avoids them being affected by 
# any mutations to the original list

# Revised code:
import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])