#!/usr/bin/python3
""" This is a simple calculator module"""

# Definition of the simple operations starting with addition
def add(num1: int, num2: int) -> int:
    return num1 + num2


def sub(num1: int, num2: int) -> int:
    """The function subtracts two integers"""
    return num1 - num2

def mul(num1, num2):
    """Multiplication of two numbers"""
    return num1 * num2


def div(num1, num2):
    """Divides two numbers"""

    return num1 / num2

print("Select your suitable operation from the list below:\n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n")

operation = int(input("Enter your preferred operant (1, 2, 3 or 4): "))
first_number = int(input("Enter first number: "))
sec_number = int(input("Enter second number: "))

if operation == 1:
    print(first_number, "+", sec_number, "=", add(first_number, sec_number))
elif operation == 2:
    print(first_number, "-", sec_number, "=", sub(first_number, sec_number))
elif operation == 3:
    print(first_number, "*", sec_number, "=", mul(first_number, sec_number))
elif operation == 4:
    print(first_number, "/", sec_number, "=", div(first_number, sec_number))
else:
    print("invalid")
