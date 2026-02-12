# PROCESS
# Given a list of strings, sort the list based on the highest number
# of adjacent consonants a string contains and return the sorted list.
# 
# Inputs: A list of strings
# Outputs: The same list of strings, but sorted high to low (by adjacent consonants)

# Explicit rules:
    # If two strings contain the same highest number of adjacent consonants, 
    # they should retain their original order.
    # Consonants are considered adjacent if they are next to each other in the same word, or
    # if there is space between two consonants in adjacent words.
# Implicit:
    # Spaces do not count as consonants OR non-consonants (should be skipped)
    # 

# Questions:
# What if a string has a non-alphabetic symbol? 
# Can I assume all elements in the list will be strings, and English language?


# EXAMPLES AND TEST CASES
'''
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
'''
# strings with 0 adjacent consonants (but a non-zero number of consonats)
# should not be re-sorted


# DATA STRUCTURE
# My input and output is a list
# Could use a dictionary that assigns key-value pairs of string with integer
# of adjacent consonants, but possibly not needed.

# ALGORITHM
# For each string, find its max consonant score using a Helper algorithm
# Sort the original list using the score from step 1
# Return the sorted list

# Helper algorithm #1: get_consonant_score
# input: a string
# output: an integer
# Steps:
    # remove spaces from the string
    # initialize 'max_count' to 0
    # initialize 'current_run' to 0
    # loop through each character in the input string:
        # if the character is a consonant:
            # concatenate it to the 'current_run'
        # If the letter is a vowel
            # if the 'current_run' has a length greater
            # than the current `max_count':
                # If the 'current_run' has a length greater than 1
                    # Set the 'max_count' to the length of the 'current_run'
            # Reset 'currrent_run' to an empty string
# Return 'max_count'

# CODE
def sort_by_consonant_count(list_of_strings):
    list_of_strings.sort(key=get_consonant_score, reverse=True)
    return list_of_strings

def get_consonant_score(string):
    string = ''.join(string.split(' '))
    max_count = 0
    current_run = ''
    for char in string:
        if char in 'bcdfghjklmnpqrstvwxyz':
            current_run += char
            if len(current_run) > max_count:
                if len(current_run) > 1:
                    max_count = len(current_run)
        else:
            if len(current_run) > max_count:
                if len(current_run) > 1:
                    max_count = len(current_run)
            current_run = ''
    return max_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']