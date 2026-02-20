# Given a dictionary and a list of keys,
# produce a new dictionary that only contains
# the key/value pairs for the specified keys.

# Examples
# {'red': 1, 'green': 2, 'blue': 3, 'yellow': 4,} and ['red', 'blue']
# -->{'red': 1, 'blue': 3}

# DS
# Input is a list, and a dict
# Output will be a new dict
# Might build intermediate list of keys

# Alg
# Define func keep_keys that receives two arguments: a dict and a list
# Intialize a new empty dict
# Iterate over the list
# Use dict.get() to check for existence in dict of each key in list
    # If key is returned, append to new_dict
# Return dict


# Code
'''
def keep_keys(input_dict, keys_list):
    result = {}
    for key in keys_list:
        if key in input_dict:
            result[key] = input_dict[key]
    return result
'''
    
def keep_keys(input_dict, keys_list):
    return {key: input_dict[key] for key in keys_list if input_dict.get(key)}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True