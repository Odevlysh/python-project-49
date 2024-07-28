# brain-even

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'

def get_question_and_answer():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, correct_answer

def main():
    from brain_games.game_engine import run_game
    run_game(brain_even)

if __name__ == '__main__':
    main()
