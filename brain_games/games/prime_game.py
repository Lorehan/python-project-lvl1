import random


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isPrime(number):
    if number % 2 == 0:
        return number == 2
    denominator = 3
    while denominator ** 2 <= number and number % denominator != 0:
        denominator += 2
    return denominator ** 2 > number


def get_question():
    question = random.randint(2, 100)
    if isPrime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
