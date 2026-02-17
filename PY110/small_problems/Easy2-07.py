# Write a function that takes two list arguments, 
# each containing a list of numbers, 
# and returns a new list that contains the product
# of each pair of numbers from the arguments 
# that have the same index. 
# You may assume that the arguments contain the same number of elements.


# Example
# [3, 5, 7] and [9, 10, 11] --> [27, 50, 77]

# Data
# Input is two lists
# Output is a list

# Algorithm
# This problem is built for the zip function
# Initialize an empty list
# Zip the items from both lists in a for loop
    # multiply the items together
    # append the product



def multiply_list(list1, list2):
    prod_list = []
    for num1, num2 in zip(list1, list2):
        prod = num1 * num2
        prod_list.append(prod)
    return prod_list


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True