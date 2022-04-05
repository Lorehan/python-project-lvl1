#!/usr/bin/env python

import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers_count = 0
    while correct_answers_count < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
