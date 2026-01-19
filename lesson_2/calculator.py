# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user to choose an arithmetic operation.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt(MESSAGES['welcome'])

while True:
    prompt(MESSAGES['first_num'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid'])
        number1 = input()

    prompt(MESSAGES['second_num'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid'])
        number2 = input()

    prompt(MESSAGES['operation'])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['wrong_num'])
        operation = input()

    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) / int(number2)

    prompt((MESSAGES['result']) + f' {output}')

    prompt(MESSAGES['another'])
    again = input()

    if not again or again[0].lower() != 'y':
        prompt(MESSAGES['thanks'])
        break