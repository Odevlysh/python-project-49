#!/usr/bin/env python3


import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name


def congratulate_user(name):
    print(f"Congratulations, {name}!")


# if __name__ == '__main__':
    # main()
