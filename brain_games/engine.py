import prompt


ROUNDS_COUNT = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(ROUNDS_COUNT):
        (question, correct_answer) = game.get_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            return print(
                f"'{answer}' is wrong answer ;(. ",
                f"Correct answer was '{correct_answer}'.\n",
                f"Let's try again, {name}!", sep='')
    print(f'Congratulations, {name}!')
