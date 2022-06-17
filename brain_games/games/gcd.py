from random import randint
import math


condition = 'Find the greatest common divisor of given numbers.'


def main_part():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    expression = f'{num1} {num2}'
    result = math.gcd(num1, num2)
    return result, expression
