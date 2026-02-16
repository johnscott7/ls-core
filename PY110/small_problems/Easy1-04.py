# Write a function that takes a list of numbers and returns
# a list with the same number of elements, but with each element's
# value being the running total from the original list.

# Examples
# ([2, 5, 13]) --> (2, 7, 20])
# ([3]) --> ([3])
# ([]) --> ([])

# Data structure
# Input will be a list
# Initialize a new list
# Build a new list summing each of the previous elements
# Will also need to intialize a placaholder sum_total value
# that will hold the intermediate sum_total over each loop

# Algorithm
# define running_total(passed_list):
    # for each list item in passed_list:
        # Sum total = existing sum total + item
        # Append sum total to a new list


def running_total(num_list):
    sum_list = []
    sum_total = 0
    for num in num_list:
        sum_total += num
        sum_list.append(sum_total)
    return sum_list

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True

#