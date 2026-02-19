# Write a function that takes a string, 
# doubles every consonant in the string, 
# and returns the result as a new string. 
# The function should not double vowels ('a','e','i','o','u'), 
# digits, punctuation, or whitespace.

# Examples

# ('String') == "SSttrrinngg"
# ('Hello-World!') == "HHellllo-WWorrlldd!"
# ('July 4th') == "JJullyy 4tthh"
# ('') == ""

# DS
# Input is a string
# Output will be a string
# Inter DS will be a list 

# Algorithm
# Initialize an empty list
# Iterate over the string argument
    # if char is in alphabet (write out all consonants, lower and UPPER)
        # append char * 2 into the list
    # otherwise
        # append char into the list
# join the list on '' to a string, and return it

# Code:
def double_consonants(string):
    double_char_list = []
    for char in string:
        if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            double_char_list.append(char * 2)
        else:
            double_char_list.append(char)
    return ''.join(double_char_list)


# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")