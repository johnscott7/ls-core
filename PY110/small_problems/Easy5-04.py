# Write a function that takes a string as an argument
# and returns a list that contains every word from the
# string, with each word followed by a space and the word's
# length. If the argument is an empty string or if no argument
# is passed, the function should return an empty list.

# You may assume that every pair of words in the string will be separated by a single space.

# Examples

# 'cow sheep chicken'
# ['cow 3', 'sheep 5', 'chicken 7']

# 'baseball hot dogs and apple pie'
# ['baseball 8', 'hot 3', 'dogs 4', 'and 3', 'apple 5', 'pie 3']

# "It ain't easy, is it?"
# ['It 2', "ain't 5", 'easy, 5', 'is 2', 'it? 3']

# 'Supercalifragilisticexpialidocious'

# ('') --> []
# () --> []

# DS
# Input is a string
# Output will be a list of string elements

# Alg
# Def func word_lengths that accepts a string argument
# If len string input is zero
    # return an empty list
# split strings into a list on whitespace and assign to word_list
# Initialize an empty list
# For each element in word_list
    # Append element and len(element) to empty list (use f-string)
# Return new_list


# Code
def word_lengths(words=''):
    if not words:
        return []
    word_list = words.split(' ')
    result = []
    for word in word_list:
        result.append(f'{word} {len(word)}')
    return result

# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True