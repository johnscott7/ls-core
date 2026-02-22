# Write a function that takes a list argument
# and returns a new list that contains the values
# from the input list in sorted order.
# The function should sort the list using the merge
# sort algorithm as described above. You may assume
# that every element of the list will have the same
# data type: either all numbers or all strings.

# Feel free to use the merge function you wrote in the previous exercise.

# Examples
# All of these examples should print True
# [9, 5, 7, 1]) --> [1, 5, 7, 9])
# [5, 3]) --> [3, 5])
# [6, 2, 7, 1, 4]) --> [1, 2, 4, 6, 7])
# [9, 2, 7, 6, 8, 5, 0, 1]) --> [0, 1, 2, 5, 6, 7, 8, 9])

# ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
#             'Kim', 'Bonnie']
# -->
# ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
#             'Sue', 'Tyler']

# DS
# Input is a single list
# Output is a single list
# Will have many intermediate nested lists inbetween

# Alg
# def function merge_sort that accepts a list
# final_length = len(list)
# Create a while loop that will run so long as len(list) > 1
    # lst_divide(list)

# While loop that will run until len(list) = final_length
    # for sublist in list
        # merge(sublist)

# Helper function lst_divide(lst):
    # determine halfway number of list length
    # create a first half list
    # create a second half list
    # mutate the original list to be [first_half, second_half]

# Easier to handle recursively than to use a helper function!
# lst_divide function above is on the right track, but
# then needs to call itself on each half-list, recursively.

# Code
def merge(list1, list2):
    copy1 = list1[:]
    copy2 = list2[:]
    result = []

    while copy1 and copy2:
        if copy1[0] <= copy2[0]:
            result.append(copy1.pop(0))
        else:
            result.append(copy2.pop(0))

    return result + copy1 + copy2

def merge_sort(original_list):
    if len(original_list) <= 1:
        return original_list
    halfway = len(original_list) // 2
    first_list = original_list[:halfway]
    second_list = original_list[halfway:]
    first_list = merge_sort(first_list)
    second_list = merge_sort(second_list)
    return merge(first_list, second_list)


# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)