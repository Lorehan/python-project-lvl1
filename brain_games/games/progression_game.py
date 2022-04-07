import random


RULE = 'What number is missing in the progression?'


def get_question():
    start_progression = random.randint(1, 50)
    end_progression = random.randint(100, 150)
    step = random.randint(-10, 10)
    if step == 0:
        step += 1
    if step > 0:
        progression = list(range(
            start_progression,
            end_progression,
            step))[0:10]
    else:
        progression = list(range(
            end_progression,
            start_progression,
            step))[0:10]
    correct_answer = random.choice(progression)
    progression[progression.index(correct_answer)] = '..'
    question = ' '.join(map(str, progression))
    return question, str(correct_answer)
