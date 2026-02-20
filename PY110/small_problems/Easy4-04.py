# Given a dictionary, 
# return its keys sorted by the values associated with each key.

# Examples
# {'p': 8, 'q': 2, 'r': 6} --> ['q', 'r', 'p']

# DS
# input is a dict
# output is a list

# Alg
# Define a func order_by_value that accepts a dict argument
# return a sorted list of the dictionary keys, but sort
# using a key, where the key is the dictionary get method 
# (which obtains the dict values)


def order_by_value(my_dict):
    return sorted(my_dict, key=my_dict.get)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True
