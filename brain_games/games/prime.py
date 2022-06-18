from random import randint


condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def main_part():
    number = randint(1, 100)
    expression = number
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        result = 'yes'
    else:
        result = 'no'
    return result, expression

