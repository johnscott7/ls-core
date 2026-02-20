# You have a function that is supposed to 
# reverse a string passed as an argument. 
# However, it's not producing the expected output. 
# Explain the bug, and provide a solution.
''' buggy code:
def reverse_string(string):
    for char in string:
        string = char + string

    return string
'''
# This code is attemping to reverse the string
# But is repeately re-assigning the string variable
# to an ever growing string that also contains the
# original string.

# Should instead build a new string on 
# a new_string variable

def reverse_string(string):
    new_string = ""
    for char in string:
        new_string = char + new_string

    return new_string

print(reverse_string("hello"))# == "olleh")