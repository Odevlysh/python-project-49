# brain-prime

import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():

    question = random.randint(1, 20)

    if question == 1:
        correct_answer = 'no'

    elif question == 2 or question == 3:
        correct_answer = 'yes'

    else:
        i = 2
        correct_answer = 'yes'

        while i * i <= question:
            if question % i == 0:
                correct_answer = 'no'
                break

            i += 1

    return question, correct_answer
