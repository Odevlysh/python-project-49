# brain-prime

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
RANGE_START = 0
RANGE_END = 20


def is_prime(question):
    if question <= 1:
        return False

    elif question == 2 or question == 3:
        return True

    else:
        i = 2
        while i * i <= question:
            if question % i == 0:
                return False
            i += 1
        return True


def get_question_and_answer():
    question = random.randint(RANGE_START, RANGE_END)

    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
