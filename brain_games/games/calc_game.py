import random


RULE = 'What is the result of the expression?'
OPERATIONS = ('+', '-', '*')


def get_question():
    operation = random.choice(OPERATIONS)
    first_number = random.randint(1, 50)
    second_number = random.randint(1, 50)
    if operation == '+':
        question = f'{first_number} + {second_number}'
        correct_answer = first_number + second_number
    elif operation == '-':
        question = f'{first_number} - {second_number}'
        correct_answer = first_number - second_number
    else:
        question = f'{first_number} * {second_number}'
        correct_answer = first_number * second_number
    return question, str(correct_answer)
