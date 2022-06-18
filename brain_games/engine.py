#!/usr/bin/env python3
import prompt


def engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.condition)
    i = 0
    while i <= 2:
        result, expression = game.main_part()
        print(f'Question: {expression}')

        answer = ''
        while answer == '':
            answer = input('Your answer: ')

        if answer == result:
            print('Correct!')
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {result}.\nLet's try again, " + name + '!')
            break
        i += 1
    else:
        print('Congratulations, ' + name + '!')
