def check_eligibility(marks, attendance, backlog):
    if marks >= 60 and attendance >= 75 and backlog is False:
        return "Eligible"
    return "Not Eligible"


if __name__ == "__main__":
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance percentage: "))
    backlog_input = input("Do you have a backlog? (true/false): ").strip().lower()
    backlog = backlog_input == "false"
    print(check_eligibility(marks, attendance, backlog))
