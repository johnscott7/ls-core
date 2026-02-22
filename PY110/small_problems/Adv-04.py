# Write a function that takes two sorted lists
# as arguments and returns a new list that contains
# all the elements from both input lists in ascending
# sorted order. 
# You may assume that the lists contain either all integer values or all string values.

# You may not provide any solution that requires
# you to sort the result list. 
# You must build the result list one element at a time in the proper order.

# Your solution should not mutate the input lists.

# Examples
# All of these examples should print True
# [1, 5, 9], [2, 6, 8] --> [1, 2, 5, 6, 8, 9]
# [1, 1, 3], [2, 2] --> [1, 1, 2, 2, 3]
# [], [1, 4, 5] --> [1, 4, 5]
# [1, 4, 5], [] --> [1, 4, 5]

# ['Alice', 'Kim', 'Pete', 'Sue']
# ['Bonnie', 'Rachel', 'Tyler']
# -->
# ['Alice', 'Bonnie', 'Kim', 'Pete',
# 'Rachel', 'Sue', 'Tyler']

# DS
# Input is two lists
# Output is one list

# Alg
# def function merge that accepts two list arguments
# Combine elements into a single list
# Create result = []
# While the combo list is not empty:
    # Assume first element is the smallest
    # Set min_index = 0
    # Iterate i from 1 to length of list (non-inclusive)
        # If list[i] is less than list[min_index]
            # update min_index
    # Append the item at min_index to result list
    # Remove the element at min_index from combo list
# return result list


# Code
def merge(list1, list2):
    combo = list1 + list2
    result = []

    while combo:
        min_idx = 0
        for i in range(1, len(combo)):
            if combo[i] < combo[min_idx]:
                min_idx = i
        result.append(combo[min_idx])
        combo.pop(min_idx)
    return result

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)