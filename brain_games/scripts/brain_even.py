#!/usr/bin/env python3

def main():
    # import prompt
    import random
    from brain_games.cli import welcome_user

    # print("Welcome to the Brain Games!")
    # name = prompt.string("May I have your name? ")
    # print(f'Hello, {name}!')

    name = welcome_user()
    
    print('Answer "yes" if the number is even, otherwise answer "no"')

    counter = 0
    while counter < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input().lower()

        if answer == "yes" and number % 2 == 0 or answer == "no" and number % 2 != 0:
            print("Correct!")
            counter += 1
        else:
            correct_answer = "yes" if number % 2 == 0 else "no"
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name} ")
            counter = 0

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
