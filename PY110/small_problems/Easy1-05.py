# Write a function that takes a string consisting of zero or more 
# space-separated words and returns a dictionary that shows
# the number of words of different sizes.
# Words consist of any sequence of non-space characters.


# Examples
# string = 'Four score and seven' -> {4: 1, 5: 1, 3: 1, 6: 1}
# 'Hey diddle diddle, the cat and the fiddle!' -> {3: 5, 6: 1, 7: 2}

# Data Structure
# Input is a string
# Output is a dict

# First, initialize an empty dict
# Will need to split words on whitespace and assign to a list
# Can put into a list from there, measure length of each element
# for each element in the list, either create a new dict entry, or,
# if that dict entry exists, add one more to the key value
# Can potentially use get() for this, with the default return value being 1
# (not sure this allows for adding one to an existing key-value pair though)


# Code
def word_sizes(words):
    word_dict = {}
    word_list = words.split()
    for word in word_list:
        length = len(word)
        if length in word_dict:
            word_dict[length] += 1
        else:
            word_dict[length] = 1
    return word_dict

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})