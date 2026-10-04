def check_marks(marks):
    if marks >= 75:
        return "Distinction"
    if marks >= 35:
        return "Pass"
    return "Fail"


if __name__ == "__main__":
    marks = int(input("Enter marks: "))
    print(check_marks(marks))
