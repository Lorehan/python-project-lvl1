import random


RULE = 'What number is missing in the progression?'


def get_progression(initial_term, last_term, common_difference):
    if common_difference == 0:
        common_difference += 1
    if common_difference > 0:
        progression = list(range(
            initial_term,
            last_term,
            common_difference))[0:10]
    else:
        progression = list(range(
            last_term,
            initial_term,
            common_difference))[0:10]
    return progression


def get_string_progression(progression, term):
    progression[progression.index(term)] = '..'
    string_progression = ' '.join(map(str, progression))
    return string_progression


def get_question():
    initial_term = random.randint(1, 50)
    last_term = random.randint(100, 150)
    common_difference = random.randint(-10, 10)
    progression = get_progression(initial_term, last_term, common_difference)
    correct_answer = random.choice(progression)
    question = get_string_progression(progression, correct_answer)
    return question, str(correct_answer)
