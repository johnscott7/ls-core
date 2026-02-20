# We want to create a function that
# appends a given value to a list. 
# However, the function seems to be behaving unexpectedly.
# Fix the code.

'''Buggy code:
def append_to_list(value, lst=[]):
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])
'''

# Notes
# This function attempts to append a value
# to a list, and does so succesfully, but because
# the default value is mutable, it means each 
# successive call of the function will mutate the
# same object.

# This is fixed by assigned a default value of None
# to the list, since None is not mutable, and therfore
# each successive function call which initiate a new
# and empty list object (when the list is not passed
# as a parameter).


# Revised code:
def append_to_list(value, lst=None):
    if lst is None:
        lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])