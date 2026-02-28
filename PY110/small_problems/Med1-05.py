# Write a function that takes a string as an argument 
# and returns that string with every occurrence of a 
# "number word" -- 'zero', 'one', 'two', 'three', 'four',
# 'five', 'six', 'seven', 'eight', 'nine' -- converted to its 
# corresponding digit character.

# You may assume that the string does not contain any punctuation.

# Examples
# see below

# DS
# Input is a string of words
# Output will be a string
# Dictionary for string to digits
# list for mutating

# Alg
# Before starting function scope,
# build dictionary of 'word': num
# def function that accepts a string
# conver string to list on .split()
# build dictionary of 'word': num
# Initialize a new list
# iterate over the list
# if word in dictionary.keys()
    # replace with dictionary value
# else
    # leave word as is
# return a string by joining the list on ' '

# Code

word_to_num  = {'zero': 0, 'one': 1, 
                'two': 2, 'three': 3,
                'four': 4, 'five': 5,
                'six': 6, 'seven': 7,
                'eight': 8, 'nine': 9}

def word_to_digit(words):
    word_list = words.split()
    result = []
    for word in word_list:
        if word in word_to_num:
            result.append(str(word_to_num[word]))
        else:
            result.append(word)
    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True