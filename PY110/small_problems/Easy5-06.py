# Write a function that takes a list of numbers 
# and returns the sum of the sums of each leading 
# subsequence in that list. Examine the examples to 
# see what we mean. You may assume that the list always 
# contains at least one number.


# Examples
# [3, 5, 2]) --> 21)
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

# [1, 5, 7, 3]) --> 36)
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

# [1, 2, 3, 4, 5]) --> 35)
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

# [4]) --> 4

# DS
# Input is a list
# Output will be an int
# Will need an intermediate data structure, either a list or int
# that maintains or builds its value outside of the loop

# Alg
# def func sum_of_sums to accept a list argument
# Initialize sums_list = []
# Initialize sub_total = 0
# Iterate over the list
    # define sub_total += element
    # append sub_total to total_sum list
# return sum of total_sum list

# Code
# First, using a list
'''
def sum_of_sums(num_list):
    sums_list = []
    sub_total = 0
    for num in num_list:
        sub_total += num
        sums_list.append(sub_total)
    return sum(sums_list)
'''

# Could also achieve with an int
# Same general approach
def sum_of_sums(numbers):
    total = 0
    sub_total = 0
    for num in numbers:
        sub_total += num
        total += sub_total
    return total

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True