# Write a function that takes a string and returns a dictionary containing the following three properties:

# the percentage of characters in the string that are lowercase letters
# the percentage of characters that are uppercase letters
# the percentage of characters that are neither
# All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

# You may assume that the string will always contain at least one character.

# Problem
# String of words/letter/special characters will be passed
# Does whitespace count as a character? I will assume yes.
# Want to get percentages of total string length that correspond to
    # lowercase letters
    # uppercase letters
    # neither
# No need to handle empty string cases
# Make sure to format numbers as two with :02d or
# decimals with two as :.2f with f-strings

# Example
# 'AbCd +Ef' --> 
# {'lowercase': "37.50", 'uppercase': "37.50", 'neither': "25.00", }
# Can see from this example it IS including whitespace
# lowercase here is 3/8, uppercase is 3/8, neither is 2/8

# Data Structures
# Input is a string of characters
# Output is a dictionary with three key-value pairs
# keys are 'lowercase', 'uppercase', 'neither'
# values are strings representing the percentages of total

# Might use a set of accumulating ints as intermediate DS,
# such as total_char, lower_char, upper_char, other_char
# This would allow for easy % calculation at the end

# Could also build lists and take total len of all three
# lists at the end to calculate percentage. Either way

# Alg
# define letter_percentage to take a string argument s
# Initiliaze my character counts:
    # upper_char = 0, lower_char = 0, other_char = 0, total_char = 0
# Iterate over the string s
    # Build flow control
    # If char.isalpha():
        # if char.isupper():
            # Increment upper_char by 1
            # increment total_char by 1
        # else
            # increment lower_char  by 1
            # increment total_char by 1
    # else
        # increment other_char by 1
        # increment tota_char by 1
# After iteration is complete, assign variables for my values
# lower_percent = lower_char / total_char
# upper_percent = upper_char / total_char
# neither_percent = other_char / total_char
# Intialize an empty dict result = {}
# Add key-value pairs for all three, using f-string formatting
# result['lowercase'] = f'{lower_percent:.2f}'
# result['uppercase'] = f'{upper_percent:.2f}'
# result['neither'] = f'{neither_percent:.2f}'
# return the dictionary

# Note: Not sure if/how to specify d and f in one go
# Maybe something like f'{neither_percent:02d, .2f}
# Will need to validate lengths for both whole number and decimals are correct
# Follow-up note: I needed to multiply this value by 100. The problem 
# did not actually ask for 0% to be shown as 00.00%, so the .02d approach was
# unnecessary.


# Code
def letter_percentages(s):
    total_char = 0
    upper_char = 0
    lower_char = 0
    other_char = 0
    for char in s:
        if char.isalpha():
            if char.isupper():
                upper_char += 1
                total_char += 1
            else:
                lower_char += 1
                total_char += 1
        else:
            other_char += 1
            total_char += 1
    upper_percent = (upper_char / total_char) * 100
    lower_percent = (lower_char / total_char) * 100
    neither_percent = (other_char / total_char) * 100
    result = {}
    result['lowercase'] = f'{lower_percent:.2f}'
    result['uppercase'] = f'{upper_percent:.2f}'
    result['neither'] = f'{neither_percent:.2f}'
    return result

expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)
