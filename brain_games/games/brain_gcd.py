# brain-gcd

import random
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
RANGE_START = 1
RANGE_END = 200


def get_question_and_answer():
    a = random.randint(RANGE_START, RANGE_END)
    b = random.randint(RANGE_START, RANGE_END)

    question = f'{str(a)} {str(b)}'

    correct_answer = gcd(a, b)

    return question, str(correct_answer)
