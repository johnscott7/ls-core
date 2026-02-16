# Given a string of words separated by spaces, 
# write a function that swaps the first and last letters of every word.

# Assume that every word contains at least one letter, 
# and that the string will always contain at least one word. 
# You may also assume that each string contains nothing but words and spaces, 
# and that there are no leading, trailing, or repeated spaces.

# Examples
# Start with a string
# It doesn't specify, so will assume we want to 
# return a string

# Algorithm
# Split the words into a list on whitespace
# intialize a new empty list
# build the new word one time
    # Seems like could just manually concatenate this
# Join words from list on ' ' back into a string
# Return the final string




def transform_word(word):
    if len(word) < 2:
        return word
    return word[-1] + word[1:-1] + word[0]

def swap(words):
    word_list = words.split()
    new_list = []
    for word in word_list:
        new_list.append(transform_word(word))
    return ' '.join(new_list)

# Using a transformation
def swap_2(words):
    words_list = words.split()
    new_list = [transform_word(word) for word in words_list]
    return ' '.join(new_list)



print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")   # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

print(swap_2('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")   # True
print(swap_2('Abcde') == "ebcdA")            # True
print(swap_2('a') == "a")                    # True