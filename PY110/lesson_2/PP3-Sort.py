# Sort the following list of numbers first in ascending order as string values.
# Then, sort the list in descending order as string values. 
# Both the list passed to the sorting function and the returned list 
# should contain numbers, not strings.
# You can mutate the original list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# Will make a custom function to pass as key
def num_to_strings(my_num):
    return str(my_num)

lst.sort(key = num_to_strings)
print(lst)

lst.sort(key = num_to_strings, reverse = True)
print(lst)