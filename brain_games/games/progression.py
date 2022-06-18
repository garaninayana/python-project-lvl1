from random import randint

condition = 'What number is missing in the progression?'


def main_part():
  first_num = randint(1, 50)
  difference = randint(1, 10)
  quantity = 10
  missing_num = randint(0, 9)
  missing_num_index = 0
  expression = ''

  while missing_num_index < quantity:
    if missing_num == missing_num_index:
      expression = f'{expression} ..'  
      missing_num_index += 1
    else:
      num = f'{first_num + difference * missing_num_index}'
      expression = f'{expression} {num}' 
      missing_num_index += 1 
  result = first_num + difference * missing_num
  return str(result), expression
