import random


RULE = 'What is the result of the expression?'


def get_question():
    operation_selection = random.randint(1, 3)
    first_number = random.randint(1, 50)
    second_number = random.randint(1, 50)
    if operation_selection == 1:
        question = f'{first_number} + {second_number}'
        correct_answer = first_number + second_number
    elif operation_selection == 2:
        question = f'{first_number} - {second_number}'
        correct_answer = first_number - second_number
    else:
        question = f'{first_number} * {second_number}'
        correct_answer = first_number * second_number
    return question, str(correct_answer)
