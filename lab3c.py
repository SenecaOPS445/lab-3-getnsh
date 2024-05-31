#!/usr/bin/env python3
'''Lab 3 Inv 2 function operate '''
# Author ID: gchawla4@myseneca.ca

def operate(number1, number2, operator):
    # Perform addition
    if operator == 'add':
        return number1 + number2
    # Perform subtraction
    elif operator == 'subtract':
        return number1 - number2
    # Perform multiplication
    elif operator == 'multiply':
        return number1 * number2
    # Return error message for unknown operator
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'


if __name__ == '__main__':
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))