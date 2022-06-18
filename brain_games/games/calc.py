#!/usr/bin/env python3
from random import randint
from random import choice


condition = 'What is the result of the expression?'


def main_part():
    number1 = randint(20, 50)
    number2 = randint(1, 9)
    symbol = choice(['+', '-', '*'])
    expression = f'{number1} {symbol} {number2}'
    result = str(eval(expression))
    return result, expression
