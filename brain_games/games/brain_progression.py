# brain-progression

import random

DESCRIPTION = 'What number is missing in the progression?'


def get_question_and_answer():
    progression = [random.randint(0, 100)]
    common_difference = random.randint(1, 10)
    hidden_index = random.randint(0, 9)

    for i in range(0, 9):
        progression.append(progression[i] + common_difference)

    correct_answer = str(progression[hidden_index])

    question = ''
    for i in range(0, 10):
        if i == hidden_index:
            question += '.. '
        else:
            question += str(progression[i]) + ' '

    return question, correct_answer
