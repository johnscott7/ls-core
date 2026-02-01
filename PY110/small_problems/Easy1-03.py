# Write a function named sum_of_sums that takes a list of numbers and returns the sum
# of the sums of each leading subsequences in that list

# Examples
# Input (3, 5, 2) -> Output 21 via (3) + (3 + 5) + (3 + 5 + 2)
# Input [1, 5, 7, 3] -> Output 36 via (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3)

# Data 
# Input will be a list of ints
# Output will be a single int

# Algorithm
# Receive a list passed to the function as an argument
# Initialize a new variable sum_of_sums and intermediate_sum
# Iterate through this list, adding each value to intermediate_sum

# Code
def sum_of_sums(numbers):
    intermediate_sum = 0
    total_sum = 0
    for num in numbers:
        intermediate_sum += num
        total_sum += intermediate_sum
    return total_sum

print(sum_of_sums([3, 5, 2])) # Expected: (3) + (3 + 5) + (3 + 5 + 2) --> 21
print(sum_of_sums([1, 5, 7, 3])) # Expected: (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36
print(sum_of_sums([4])) # Expected: 4
print(sum_of_sums([1, 2, 3, 4, 5])) # Expected: 35