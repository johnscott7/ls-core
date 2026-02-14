# Given the following data structure return a new list identical in structure to the original,
# but containing only the numbers that are multiples of 3.

# Solve this first without a comprehension, 
# then solve using a comprehension.

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]


# Expected output:
# [[], [3, 12], [9], [15, 18]]

def mult_of_3(lst_of_lsts):
    new_list = []
    for sublists in lst_of_lsts:
        new_sublist = []
        for num in sublists:
            if num % 3 == 0:
                new_sublist.append(num)
        new_list.append(new_sublist)
    return new_list

print(mult_of_3(lst))
                
new_list = [[num for num in item if num % 3 == 0] for item in lst]
print(new_list)