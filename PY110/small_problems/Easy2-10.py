# Write a function that takes one argument, 
# a list of integers, and returns the average of all the integers 
# in the list, rounded down to the integer component of the average. 
# The list will never be empty, and the numbers will always be positive integers.

# Examples
# [1, 5, 87, 45, 8, 8 --> 25        # True
# [9, 47, 23, 95, 16, 52] --> 40)     # True
# [7] --> 7  

# Data
# Input is a list of ints
# Output is an int

# Algorithm
# Intialize a variable start value at 0
# For loop iterating across the list
    # Add each value to the initial variable
# Divide by length of the list using floor division
# Return the int

def average(int_list):
    total_value = 0
    for num in int_list:
        total_value += num
    return total_value // len(int_list)
   
    
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True