# Write a program that solicits six (6) numbers from the user and prints a message 
# # that describes whether the sixth number appears among the first five.

input_request = ['1st', '2nd', '3rd', '4th', '5th', 'last']
numbers = []

for label in input_request:
    value = int(input(f'Enter the {label} number: '))
    numbers.append(value)

first_five = numbers[:-1]
last_number = numbers[-1]
numbers_list = ",".join(map(str, first_five))
if last_number in first_five:
    print(f"{last_number} is in {numbers_list}.")
else:
    print(f"{last_number} is not in {numbers_list}.")
