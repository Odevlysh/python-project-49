# brain-calc

import random

DESCRIPTION = 'What is the result of the expression?'
RANGE_START = 1
RANGE_END = 100


def get_question_and_answer():
    operators = ['+', '-', '*']
    a = random.randint(RANGE_START, RANGE_END)
    b = random.randint(RANGE_START, RANGE_END)
    operator = random.choice(operators)

    if operator == '+':
        correct_answer = a + b
    elif operator == '-':
        correct_answer = a - b
    elif operator == '*':
        correct_answer = a * b

    question = f'{a} {operator} {b}'
    return question, str(correct_answer)
