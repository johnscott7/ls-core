# Write a function that takes a list of integers 
# between 0 and 19 and returns a list of those integers 
# sorted based on the English word for each number:

# zero, one, two, three, four, five, six, seven, eight, nine, 
# ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen

# DS
# Input is a list
# Output is a list
# Will want to use a dictionary to translate between num and word of number

# Alg
# Define func alphabetic_number_sort that accepts a list argument
# Create a dictionary of key-value pairs where keys are numbers
# and values are those numbers written out in English
# Define a helper func word_conversion that takes a number argument
    # This function should pass the number to the dict and return the English word
# Sort the input list on a custom key, pass the function word_conversion as the key

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                    7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

NUMBER_WORDS = {0: 'zero', 1: 'one', 2: 'two',
                3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight',
                9: 'nine', 10: 'ten', 11: 'eleven',
                12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                18: 'eighteen', 19: 'nineteen'}

def word_conversion(num):
    return NUMBER_WORDS[num]

def alphabetic_number_sort(input_list):
    return sorted(input_list, key=word_conversion)

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True

