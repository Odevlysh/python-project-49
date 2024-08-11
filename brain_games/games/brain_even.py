# brain-even

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
RANGE_START = 1
RANGE_END = 100


def get_question_and_answer():
    number = random.randint(RANGE_START, RANGE_END)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, correct_answer
