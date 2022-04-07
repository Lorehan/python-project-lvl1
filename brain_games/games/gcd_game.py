import random
import math

RULE = 'Find the greatest common divisor of given numbers.'


def get_question():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)
    return question, str(correct_answer)