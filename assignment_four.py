# Flint Eller
# 10/8/18
# This program asks the user a math problem and checks the answer

import random


def get_operation():
    user_operation = input("What operation would you like? (+, -, *)")
    if user_operation == "-":
        return user_operation
    elif user_operation == "*":
        return user_operation
    else:
        return "+"


def get_max_number():
    max_number = float(input("What is the maximum number you would like?"))
    return max_number


def get_random_(max_number):
    random_ = random.randint(1, max_number)
    return random_


def send_problem(number_one, user_operation, number_two):
    user_answer = float(input(number_one, user_operation, number_two))
    return user_answer


def correct_answer(number_one, user_operation, number_two):
    if user_operation == "-":
        return number_one - number_two
    elif user_operation == "*":
        return number_one * number_two
    else:
        return number_one + number_two


def check_answer(user_answer, answer):
    if user_answer == answer:
        print("Correct, nice job!")
    else:
        print("Sorry, the correct answer is", answer, "Thanks for playing!")


def main():
    user_operation = get_operation()
    max_number = get_max_number()
    number_one = get_random_(max_number)
    number_two = get_random_(max_number)
    user_answer = send_problem(number_one, user_operation, number_two)
    answer = correct_answer(number_one, user_operation, number_two)
    check_answer(user_answer, answer)


main()
