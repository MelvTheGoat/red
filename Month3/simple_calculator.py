# Welcome to the Simple Calculator
# Select operation:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit

# Enter your choice from 1 to 5: 3
# Enter first number: 3
# Enter second number: 4

# 3.0 X 4.0 = 12.0


def addition():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return f"{num1} + {num2} = {num1 + num2}"

def subtraction():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return f'{num1} - {num2} = {num1 * num2}'

def multiplication():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return f'{num1} x {num2} = {num1 * num2}'

def division():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    return f'{num1} / {num2} = {num1 / num2}'


inpu = "Start"
while True:
    if inpu == 'Start':
        print('Welcome to the Simple Calculator')
    choice = input(
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n"
        "5. Exit\n\n"
        "Enter your choice from 1 to 5: "
    )
    if choice == '1':
        print(addition())
    elif choice == '2':
        print(subtraction())
    elif choice == '3':
        print(multiplication())
    elif choice == '4':
        print(division())
    elif choice == '5':
        break
    else:
        print("Put Valid Input")
        continue

    # choice2 = input("Another calculation:? yes/no: ")
    # if choice2 == 'yes':
    #     continue
    # elif choice2 == 'no':
    #     print("See you soon!")
    

