# Write a function that takes an integer argument 
# and returns a list containing all integers between 
# 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.


# Examples
# sequence(5) == [1, 2, 3, 4, 5]
# sequence(3) == [1, 2, 3]
# sequence(1) == [1] 

# DS
# Input is an int
# Output will be a list of integers

# Algorithm
# Define a function sequence that accepts one argument
# initialize an empty list
# iterate over a range from 1, to number + 1
    # append index number to list
# return list


# Code
def sequence(number):
    result = []
    for idx in range(1, number + 1):
        result.append(idx)
    return result

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True