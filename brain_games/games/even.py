#!/usr/bin/env python3
from random import randint


condition = 'Answer "yes" if the number is even, otherwise answer "no".'


def main_part():
    expression = randint(1, 100)
    def is_even(str):
        if expression % 2 == 0:
            return 'yes'
        else:
            return 'no'

    result = is_even(expression)  
    return result, expression
        
