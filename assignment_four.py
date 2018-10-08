# Flint Eller
# 10/8/18
# This program asks the user a math problem and checks the answer

import random


def get_operation():
    """
    This function asks the user which operator they would like to use and checks to see if it is one of the options
    :return: The given operation, if a incorrect function is given, returns as a +
    """
    user_operation = input("What operation would you like? (+, -, *) ")
    if user_operation == "-":
        return user_operation
    elif user_operation == "*":
        return user_operation
    else:
        return "+"


def get_max_number():
    """
    Asks user what they want the maximum number to be
    :return: the maximum number
    """
    max_number = float(input("What is the maximum number you would like? "))
    return max_number


def get_random_(max_number):
    """
    Gets the maximum number based on user's highest number
    :param max_number:
    :return: the random number
    """
    random_ = random.randint(1, max_number)
    return random_


def send_problem(number_one, user_operation, number_two):
    """
    Prints the problem for the user and gets input
    :param number_one:
    :param user_operation:
    :param number_two:
    :return: user's answer
    """
    print(number_one, user_operation, number_two)
    user_answer = float(input("What is the answer? "))
    return user_answer


def correct_answer(number_one, user_operation, number_two):
    """
    Finds correct answer based on user operation
    :param number_one:
    :param user_operation:
    :param number_two:
    :return:the correct answer
    """
    if user_operation == "-":
        return number_one - number_two
    elif user_operation == "*":
        return number_one * number_two
    else:
        return number_one + number_two


def check_answer(user_answer, answer):
    """
    Checks to see if user answered correctly
    :param user_answer:
    :param answer:
    :return: A message saying weather user got it right or not
    """
    if user_answer == answer:
        print("Correct, nice job!")
    else:
        print("Sorry, the correct answer is", answer, ", thanks for playing!")


def main():
    user_operation = get_operation()
    max_number = get_max_number()
    number_one = get_random_(max_number)
    number_two = get_random_(max_number)
    user_answer = send_problem(number_one, user_operation, number_two)
    answer = correct_answer(number_one, user_operation, number_two)
    check_answer(user_answer, answer)


main()
