# Given a sequence of integers, filter out instances
# where the same value occurs successively, retaining 
# only the initial occurrence. Return the refined sequence.

# Examples
# [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4] --> [1, 2, 6, 5, 3, 4]

# Non-consecutive duplicates are kept
# [1, 2, 1, 3] --> [1, 2, 1, 3]

# DS
# Input is a list of ints
# Output will be a list of ints

# Alg
# Def func unique_sequence that takes list argument
# Initiate a new empty list
# Iterate over the list using an index
    # Compare the char at idx position to char at idx + 1
    # If they are the same, do not add char to list
    # Have to handle last index case differently somehow



# Code
def unique_sequence(int_list):
    if not int_list:
        return non_sequentials
    non_sequentials = [int_list[0]]
    for num in int_list[1:]:
        if num != non_sequentials[-1]:
            non_sequentials.append(num)
    return non_sequentials

    
original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True