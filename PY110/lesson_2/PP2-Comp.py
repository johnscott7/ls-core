# Given the following data structure, return a new list with the same structure, 
# but with the values in each sublist ordered in ascending order. 
# Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

# Expected output:
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

new_list = []
for item in lst:
    new_list.append(sorted(item))
print(new_list)

my_new_list = [sorted(item) for item in lst]
print(my_new_list)