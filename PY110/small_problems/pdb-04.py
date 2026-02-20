# You have a function that should check
# whether a key exists in a dictionary and returns its value.
# However, it's raising an error. Why is that? How would you fix this code?

'''
Buggy code:
def get_key_value(my_dict, key):
    if my_dict[key]:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))
'''

# This code attempts to retrieve a value from a
# dictionary but does not have any safeguard in
# place for when the key does not exist. There
# are two ways to handle this, either with a 
# try/except block, or even more simply, using
# the dictionary get() method.
# Using the get method means the if/else block
# can be removed entirely, as it automatically
# returns None when the key does not exist.

# Revised code:
def get_key_value(my_dict, key):
    return my_dict.get(key)

print(get_key_value({"a": 1}, "b"))