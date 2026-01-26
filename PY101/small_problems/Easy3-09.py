# P
# Given a string of some words and an assortment of non-alphabetic characters,
# write a function that returns that string with all of the non-alphabetic characters replaced by spaces
# if one or more non-alphabetic characters occur in a row,
# you should only have one space in the result

# Example

# D
# Input is a messy string
# Output will be returning a cleaned string


def clean_up(messy_string):
    cleaned_string = ''
    prev_char_space = False
    for char in messy_string:
        if char.isalpha():
            cleaned_string += char
            prev_char_space = False
        else:
            if not prev_char_space:
                cleaned_string += ' '
                prev_char_space = True
    return cleaned_string

print(clean_up("---what's my +*& line?") == " what s my line ") # True
