def calculate(a, b, operator):
    match operator:
        case "+":
            result = a + b
            print(f"The result of {a} + {b} is: {result}")
        case "-":
            result = a - b
            print(f"The result of {a} - {b} is: {result}")
        case "*":
            result = a * b
            print(f"The result of {a} * {b} is: {result}")
        case "/":
            if b != 0:
                result = a / b
                print(f"The result of {a} / {b} is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Error: Invalid operator. Please use +, -, *, or /.")


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    calculate(a, b, operator)
