# Write a function that takes a list as an argument and
# returns a list that contains two elements, both of which are lists. 
# Put the first half of the original list elements in the first element 
# of the return value and put the second half in the second element. 
# If the original list contains an odd number of elements, 
# place the middle element in the first half list.

# Examples:
# [1, 2, 3, 4] --> [1, 2], [3, 4]
# [1, 5, 2, 4, 3] --> [1, 5, 2], [4, 3]

# Data
# Input is a list
# Output will be list of lists

# Algorithm
# Will need to divide the length in half using floor division (call this low_midpoint)
    # If length of input list is even
        # both lists are same length (equal to floor division value)
    # If length of input list is odd
        # first list is floor division value + 1
# Initialize two empty lists
# Create for loop iterating over input list index numbers
    # if idx less than  low_midpoint
    #   append to first list
    # if index value > low_midpoint
    #   append to second list

# Note: The below three lines was not needed. Simply do:
# Return [first list, second list]

# Initialize a final list
# Append new list 1 to final list
# Append new list 2 to final list

# Code
def halvsies(num_list):
    low_midpoint = len(num_list) / 2
    first_sublist = []
    second_sublist = []
    final_list = []
    for idx in range(len(num_list)):
        if idx < low_midpoint:
            first_sublist.append(num_list[idx])
        else:
            second_sublist.append(num_list[idx])
    return [first_sublist, second_sublist]


# Alternate approach:

def halvsies2(num_list):
    first_half_len = ((len(num_list) + 1) // 2)
    return [num_list[0:first_half_len], num_list[first_half_len:]]

print(halvsies([]))
      
'''
# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
'''