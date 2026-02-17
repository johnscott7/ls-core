# Write a function that combines two lists passed as arguments
# and returns a new list that contains all elements from both 
# list arguments, with each element taken in alternation.

# You may assume that both input lists are non-empty, 
# and that they have the same number of elements.

# Example
# [1, 2, 3], ['a', 'b', 'c'] --> [1, 'a', 2, 'b', 3, 'c']

# Data 
# Input is two lists
# Output is two lists

# Algorithm
# Initialize a new list
# For loop across range length of either list
    # Append list1[idx]
    # Append list2[idx]
# Return the new list

# Code
def interleave(list1, list2):
    result = []
    for idx in range(len(list1)):
        result.append(list1[idx])
        result.append(list2[idx])
    return result  

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True