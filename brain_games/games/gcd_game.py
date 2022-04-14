import random

RULE = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_operand, second_operand):
    while first_operand != 0 and second_operand != 0:
        if first_operand > second_operand:
            first_operand = first_operand % second_operand
        else:
            second_operand = second_operand % first_operand
    return first_operand + second_operand


def get_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    correct_answer = find_gcd(first_number, second_number)
    return question, str(correct_answer)
