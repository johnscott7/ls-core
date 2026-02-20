# We want to remove certain items
# from a set while iterating over it,
# but the code below throws an error.
# Why is that and how can we fix it?

'''Buggy code:
data_set = {1, 2, 3, 4, 5}

for item in data_set:
    if item % 2 == 0:
        data_set.remove(item)
'''

# Notes
# Sets are unordered collections, and
# as a result do not allow you to change
# size while iterating over them, because then
# Python does not know what item to look at next, or 
# which it has previously looked at in the set.

# It is not possible to achieve what this code wants 
# (mutating the initial set) but we can re-assign data_set
# to a new set with the desired items as shown in the below code.

# Revised code:
data_set = {1, 2, 3, 4, 5}
data_set = {item for item in data_set if item % 2 != 0}
