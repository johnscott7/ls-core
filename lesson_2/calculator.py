# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user to choose an arithmetic operation.
# Perform the operation on the two numbers.
# Print the result to the terminal.

LANGUAGE = 'ar'

import json
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(key):
    print(f'==> {MESSAGES[LANGUAGE][key]}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('welcome')

while True:
    prompt('first_num')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid')
        number1 = input()

    prompt('second_num')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid')
        number2 = input()

    prompt('operation')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('wrong_num')
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

    prompt('result')
    print(f"==> {output}")

    prompt('another')
    again = input()

    if not again or again[0].lower() != 'y':
        prompt('thanks')
        break