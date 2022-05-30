from random import randint
import prompt
from cli import welcome

def game_even():
  welcome()
  name = prompt.string('May I have your name? ')
  print(f'Hello, {name}!')
  print('Answer "yes" if the number is even, otherwise answer "no".')
  i = 0
  while i <= 2:
    number = randint(1, 100)
    print(f'Question: {number}')

    answer = ''
    while answer == '':
      answer = input('Your answer: ')

    def is_even(str):
      if number % 2 == 0:
        return True
      else:
        return False

      
    if answer == 'yes':
      if is_even(number) == True:
        print('Correct!')
      else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, " + name + '!')
        break
    elif answer == 'no':
      if is_even(number) == False:
        print('Correct!')
      else:
        print("'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, " + name + '!')
        break
    else:
      print("It's a wrong answer ;(.\nLet's try again,  " + name + "!")
      break
    i += 1
  else:
    print('Congratulations, ' + name + '!')
