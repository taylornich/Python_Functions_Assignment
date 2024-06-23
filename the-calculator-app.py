# question 1 task 1

def addition(a, b):
    return a + b
sum = addition(4, 7)
print(sum)


def subtraction(a, b):
    return a - b
difference = subtraction(4, 7)
print(difference)


def multiplication(a, b):
    return a * b
product = multiplication(4, 7)
print(product)

def division(a, b):
    return a / b
quotient = division(4,7)
print(quotient)

# question 1 task 2

operation = input("What operation would you like to use?")
num1 = float(input("Enter the first number you would like to use: "))
num2 = float(input("Enter the second number you would like to use: "))

if operation == "addition":
    result = num1 + num2

elif operation == "subtraction":
    result = num1 - num2

elif operation == "multiplication":
    result = num1 * num2

else:
    result = num1 / num2

print(f"Result {result}")


# question 1 task 3

import pdb

operation = input("What operation would you like to use?")
num1 = float(input("Enter the first number you would like to use: "))
num2 = float(input("Enter the second number you would like to use: "))

if operation == "addition":
    result = num1 + num2

elif operation == "subtraction":
    result = num1 - num2

elif operation == "multiplication":
    result = num1 * num2

elif operation == "division":
    if num1 or num2 ==0:
        print("Invalid")
    else:
     result = num1 / num2

else:
    print("Sorry, that operation cannot be performed.")
