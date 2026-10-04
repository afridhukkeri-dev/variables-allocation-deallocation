def check_number(num):
    # Even or Odd
    if num % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")

    # Divisible by 3
    if num % 3 == 0:
        print("The number is divisible by 3")
    else:
        print("The number is not divisible by 3")

    # Divisible by 5
    if num % 5 == 0:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    check_number(num)