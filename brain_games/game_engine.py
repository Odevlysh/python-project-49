import prompt

MAX_ROUNDS = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    counter = 0
    while counter < MAX_ROUNDS:
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}")
            counter = 0

    print(f'Congratulations, {name}!')
