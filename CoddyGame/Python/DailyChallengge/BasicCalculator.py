"""
    In this challenge, you are required to write a function that takes two numbers and an operator as input and performs the specified operation on the input numbers. The calculator should be able to perform addition, subtraction, multiplication, and division.

"""


def calculate(number_1, number_2, operator):
    if operator == '+':
        return number_1 + number_2
    elif operator == '-':
        return number_1 - number_2
    elif operator == '*':
        return number_1 * number_2
    elif operator == '/':
        return number_1 / number_2
