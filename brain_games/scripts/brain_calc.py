#!/usr/bin/env python3

# brain-calc

import random
from brain_games.cli import welcome_user, congratulate_user


def main():
    name = welcome_user()

    print('What is the result of the expression?')

    operators_list = ['+', '-', '*']
    counter = 0

    while counter < 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operator = random.choice(operators_list)

        print(f'Question: {a} {operator} {b}')
        answer = int(input())

        if operator == '+':
            correct_answer = a + b
        elif operator == '-':
            correct_answer = a - b
        elif operator == '*':
            correct_answer = a * b

        if answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.")
            print(f"Let's try again, {name}")
            counter = 0

    congratulate_user(name)


if __name__ == '__main__':
    main()
