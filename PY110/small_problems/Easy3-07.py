# Write a function that takes a string argument
# consisting of a first name, a space, and a last name. 
# The function should return a new string consisting 
# of the last name, a comma, a space, and the first name.

# Example
# 'Joe Roberts' == "Roberts, Joe"

# DS
# Input is a string
# Output is a string
# May want an intermediate list


# Algorithm
# Define function swap_name that takes a string argument
# Separate the names into a list of two elements
# Reverse the list
# Insert a comma and a whitespace as elements at positions 1 and 2
# Join the list into a string on no space



# Code
def swap_name(string):
    names = string.split()
    last_name = names[-1]
    first_name = names[0]
    return f'{last_name}, {first_name}'

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Further Exploration:
# Example:
# ('Karl Oskar Henriksson Ragvals') --> Ragvals, Karl Oskar Henriksson

def swap_long_name(string):
    names = string.split()
    last_name = names[-1]
    first_names_list = names[:-1]
    first_names = ' '.join(first_names_list)
    return f'{last_name}, {first_names}'

print(swap_long_name('Karl Oskar Henriksson Ragvals'))
