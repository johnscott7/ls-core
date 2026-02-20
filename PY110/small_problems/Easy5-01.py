# Given a dictionary where both keys and values are unique, 
# invert this dictionary so that its keys become values and its values become keys.

# Examples

# ({
#           'apple': 'fruit',
#           'broccoli': 'vegetable',
#           'salmon': 'fish',
#      }) --> {
#          'fruit': 'apple',
#          'vegetable': 'broccoli',
#          'fish': 'salmon',
#      })  # True

# DS
# Input is a dict
# Output will also be dict
# May be useful to dump values to a list in between

# Alg
# Initialize an empty list new_keys
# Iterate over dict and append existing 
# dict values into this new list list
# Initialize an empty list new_values = [dct] or [dct.keys()]
# Initialize an empty dict
# Add key-value pairs to dict by iterating over new_keys list
# For key, value in new_keys, new_values
    # new_dict[str(key)] = new_values



# Code
def invert_dict(dct):
    new_keys = [dct[key] for key in dct]
    new_values = [key for key in dct]
    new_dict = {}
    for key, value in zip(new_keys, new_values):
        new_dict[str(key)] = value
    return new_dict


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True