def arithmetic_calculator(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        if b == 0:
            return "Division by zero is not allowed"
        return a / b
    if operator == "//":
        if b == 0:
            return "Division by zero is not allowed"
        return a // b
    if operator == "%":
        if b == 0:
            return "Division by zero is not allowed"
        return a % b
    return "Invalid operator"


if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /, //, %): ")
    print(arithmetic_calculator(a, b, operator))
