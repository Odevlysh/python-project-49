# brain-progression

import random

DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_START = 0
PROGRESSION_END = 100
COMMON_DIFFERENCE_START = 1
COMMON_DIFFERENCE_END = 10
PROGRESSION_LENGTH = 10


def get_question_and_answer():
    progression = [random.randint(PROGRESSION_START, PROGRESSION_END)]
    common_difference = random.randint(
        COMMON_DIFFERENCE_START, COMMON_DIFFERENCE_END
    )

    hidden_index = random.randint(0, PROGRESSION_LENGTH - 1)

    for i in range(PROGRESSION_LENGTH - 1):
        progression.append(progression[i] + common_difference)

    correct_answer = str(progression[hidden_index])

    question = ''
    for i in range(PROGRESSION_LENGTH):
        if i == hidden_index:
            question += '.. '
        else:
            question += str(progression[i]) + ' '

    return question.strip(), correct_answer
