# You want to multiply all elements of a list by 2.
# However, the function is not returning the expected result. 
# Explain the bug, and provide a solution.

'''
Buggy code:

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])
'''
# This code is attemping to mutate the values 
# inside the list by doubling them. 
# The line item *= 2 does double the value that item 
# points to, but it does not mutate the list itself.

# We can instead iterate across the list using index
# which allows for effective mutation of the list elements.

# Revised code:
def multiply_list(lst):
    for idx in range(len(lst)):
        lst[idx] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])