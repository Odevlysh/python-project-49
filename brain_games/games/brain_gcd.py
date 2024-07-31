# brain-gcd

import random

DESCRIPTION = 'Find the greatest common divisor of given nubers.'


def get_question_and_answer():
    a = random.randint(1, 200)
    b = random.randint(1, 200)
    question = str(a) + ' ' + str(b)
    while b:
        a, b = b, a % b

    correct_answer = a

    return question, str(correct_answer)
