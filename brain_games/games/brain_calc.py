# brain-calc

import random

DESCRIPTION = 'What is the result of the expression?'

def get_question_and_answer():
    operators_list = ['+', '-', '*']
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(operators_list)

    if operator == '+':
        correct_answer = a + b
    elif operator == '-':
        correct_answer = a - b
    elif operator == '*':
        correct_answer = a * b

    question = f'{a} {operator} {b}'
    return question, str(correct_answer)

def main():
    from brain_games.game_engine import run_game
    run_game(brain_calc)

if __name__ == '__main__':
    main()
