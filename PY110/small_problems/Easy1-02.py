# Write a function that returns True if the string passed as an argument is a palinfrome, False otherwise.
# A palindrome reads the same forwards and backwards. For this problem the case matters, and all characters matter.

# Example
# (is_palindrome('madam') ==> True)
# (is_palindrome('356653') ==> True)

# Data
# input is a string
# output will be a bool

# Algorithm
# Will want to use floor division (//) to slice the len of the string. 
# Need to be careful about odd length strings

# not sure how to handle case

def is_panlindrome(any_string):
    # Will 





# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)