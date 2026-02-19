# Write a function that takes a string, 
# doubles every character in the string,
# then returns the result as a new string

# Examples
# repeater('Hello') --> "HHeelllloo"
# repeater('Good job!') --> "GGoooodd  jjoobb!!"
# repeater('') --> ""

# Data 
# Input is a string
# Output will be a string
# Intermediate structure:
# Use a list to build the new collection of elements
# Convert that list to a string at the end

# Algorithm
# Create function repeater accepting one argument
# Initialize an empty list
# Iterate over the string argument
    # For each char, append that character to the list twice
# Join all elements from that list into a string
# Return the string

# Code
def repeater(string):
    double_char_list = []
    for char in string:
        double_char_list.append(char * 2)
    return ''.join(double_char_list)


print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True