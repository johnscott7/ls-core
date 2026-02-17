# Given an unordered list and the information that 
# exactly one value in the list occurs twice 
# (every other value occurs exactly once), 
# determine which value occurs twice. 
# Write a function that finds and returns the duplicate value.

# Examples
# [1, 5, 3, 1] --> 1

# Data
# Input is a list
# Intermediate, might use a set. (wrong, see below)
# Output will be an int

# Algorithm
'''
Could turn this into a set, back into a list,
and then compare list[idx] for each one until 
an error pops up.
INCORRECT approach. List -> set -> List does NOT 
preserve original order.
'''
# Can use sort.
# Does not say whether we want to preserve 
# the original list. We will, to be safe.


# input one_dup_list
# sorted_list = sorted(one_dup_list)
#    for num in sorted_list
        # check value against next value for equality
        # if equal, return value


# Code


def find_dup(one_dup_list):
    sorted_list = sorted(one_dup_list)
    for idx, value in enumerate(sorted_list):
        if value == sorted_list[idx + 1]:
            return value
        
'''
Also possible to do this by zipping neighbors together:
 def find_dup(one_dup_list):
     sorted_list = sorted(one_dup_list)
     for left, right in zip(sorted_list, sorted_list[1:]):
         if left == right:
             return left
'''
        
print(find_dup([1, 5, 3, 1]) == 1) # True
print(find_dup([
                  18,  9, 36, 96, 31, 19, 54, 75, 42, 15,
                  38, 25, 97, 92, 46, 69, 91, 59, 53, 27,
                  14, 61, 90, 81,  8, 63, 95, 99, 30, 65,
                  78, 76, 48, 16, 93, 77, 52, 49, 37, 29,
                  89, 10, 84,  1, 47, 68, 12, 33, 86, 60,
                  41, 44, 83, 35, 94, 73, 98,  3, 64, 82,
                  55, 79, 80, 21, 39, 72, 13, 50,  6, 70,
                  85, 87, 51, 17, 66, 20, 28, 26,  2, 22,
                  40, 23, 71, 62, 73, 32, 43, 24,  4, 56,
                   7, 34, 57, 74, 45, 11, 88, 67,  5, 58,
              ]) == 73)       # True