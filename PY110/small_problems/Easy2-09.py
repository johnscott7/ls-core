# Write a function that counts the number of occurrences 
# of each element in a given list. 
# Once counted, print each element alongside the number of occurrences. 
# Consider the words case sensitive e.g. ("suv" != "SUV").

# Example
'''
Input : ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']
Output:
# your output sequence may appear in a different sequence
car => 4
truck => 3
SUV => 1
motorcycle => 2
'''

# Data
# Input is a list
# Output needs to be printed to the screen
# Intermediate data structure should probably 
# be a dict with keys: counts

# Algorithm
# Initialize an empty dictionary
# Loop through the list
    # Use get to determine if the key exists
    # If it does, increase value for that key by 1
    # If not, create that key-value pair
# Print by iterating through the dictionary, such as:
# For key, value in dictionary:
    # print(key => value)

def count_occurrences(item_list):
    item_dict = {}
    for item in item_list:
        if item_dict.get(item, 0):
            item_dict[item] += 1
        else:
            item_dict[item] = 1
    for key, value in item_dict.items():
        print(f'{key} => {value}')

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
