# Flint Eller
# 10/8/18
# This program asks the user a math problem and checks the answer

import random


def get_operation():
    user_operation = input("What operation would you like? (+, -, *)")
    return user_operation


def get_max_number():
    max_number = float(input("What is the maximum number you would like?"))
    return max_number


def get_random_one():
    max_number = get_max_number()
    random_one = random.randint(1, max_number)
    return random_one


def get_random_two():
    max_number = get_max_number()
    random_two = random.randint(1, max_number)
    return random_two


def check_operation():
    user_operation = get_operation()
    if user_operation == "+" or "-" or "*":

    else:
        user_operation = "+"



def check_answer():
    if


def main():
    get_operation()
    get_max_number()
    get_random_one()
    get_random_two()

main()