# Write a function that takes a list as an argument and 
# sorts that list using the bubble sort algorithm.
# The sorting should be done "in-place", meaning the 
# function should mutate the list. You may assume that the list
# contains at least two elements:

# Example


# Algorithm
# Iterate over the list from index 0 to 1 short of the final element
    # use tuple unpacking to swap element with element(index + 1)
# Need to figure out how to determine when it has made a full pass
# through the list without making any changes
# Will try incrementing a value to check this


# if list[idx + 1] > list[idx]
    # swap the two values in place using tuple unpacking
    # lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]



# Code
def bubble_sort(lst):
    while True:
        changes = 0
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                changes += 1
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
        if changes == 0:
            break
    return lst

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True


lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True
