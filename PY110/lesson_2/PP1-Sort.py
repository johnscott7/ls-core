# Sort the following list of numbers first in ascending order, 
# then in descending numeric order, without mutating the list.

lst = [10, 9, -6, 11, 7, -16, 50, 8]

# Desired output:
# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

my_asc_list = sorted(lst)
my_desc_list = sorted(lst, reverse = True)

print(my_asc_list)
print(my_desc_list)