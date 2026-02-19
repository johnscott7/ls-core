# Write a function that takes a string as an argument
# and returns True if all parentheses in the string
# are properly balanced, False otherwise.
# To be properly balanced, parentheses must occur in matching '(' and ')' pairs.

# Note that balanced pairs must start with a (, not a ).

# Examples
# ("What (is) this?") --> True
# ("What is) this?") --> False
# ("What (is this?") --> False
# ("((What) (is this))?") --> True
# ("((What)) (is this))?") --> False
# ("Hey!") --> True
# (")Hey!(") --> False
# ("What ((is))) up(") --> False

# DS
# input is a string
# Output is a bool
# Will need some intermediate DS to tally ( and )
    # This won't hanlde '(' before ')' however
# Could try a +/- counter, like counting cards

# Alg
# define a function is_balanced that takes a string input
# Initialize a variable count = 0
# Iterate over the string
    # For each appearance of (, add 1 to count
    # For each appearance of ), subtract 1 from count
    # If at any point count goes below zero, we break out
# if count = 0, return True
# otherwise, return Flase


def is_balanced(string):
    count = 0
    for char in string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True