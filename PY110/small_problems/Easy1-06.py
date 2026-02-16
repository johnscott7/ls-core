# Continuation from problem 5:
# Write a function that takes a string consisting of zero or more 
# space-separated words and returns a dictionary that shows
# the number of words of different sizes.

# Modify the above described function to exclude non-letters
# when determining word size.
# for example, "it's" is 3 letters, not 4


# Examples
# string = 'Four score and seven' -> {4: 1, 5: 2, 3: 1}
# 'Hey diddle diddle, the cat and the fiddle!' -> {3: 5, 6: 3}

# Data Structure
# Input is a string
# Output is a dict

# First, initialize an empty dict
# Will need to split words on whitespace and assign to a list
# 
# New addition from problem 5:
# iterate through each character of each word and only add 
# characters that are letters
# 
# Measure length of each element
# for each element in the list, either create a new dict entry, or,
# if that dict entry exists, add one more to the key value
# Can potentially use get() for this, with the default return value being 1
# (not sure this allows for adding one to an existing key-value pair though)


# Code

# Helper function for cleaning
def remove_non_letters(word):
    alpha_word = ''
    for char in word:
        if char.isalpha():
            alpha_word += char
    return alpha_word

def word_sizes(words):
    word_dict = {}
    word_list = words.split()
    for word in word_list:
        length = len(remove_non_letters(word))
        if length == 0:
            continue
        if length in word_dict:
            word_dict[length] += 1
        else:
            word_dict[length] = 1
    return word_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('@@@') == {})
print(word_sizes('') == {})