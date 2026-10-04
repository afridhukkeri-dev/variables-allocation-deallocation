def placement_eligibility(age, marks, attendance, experience, has_backlog):
    if marks >= 60 and attendance >= 75 and has_backlog is False:
        eligible = "Yes"
    else:
        eligible = "No"

    if experience == 0:
        category = "Fresher"
    elif 1 <= experience <= 2:
        category = "Junior"
    elif experience > 2:
        category = "Experienced"
    else:
        category = "Invalid experience"

    return {
        "placement_eligible": eligible,
        "candidate_category": category,
    }


if __name__ == "__main__":
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))
    attendance = float(input("Enter attendance percentage: "))
    experience = int(input("Enter experience in years: "))
    backlog_input = input("Has backlog? (yes/no): ").strip().lower()
    has_backlog = backlog_input == "yes"

    result = placement_eligibility(age, marks, attendance, experience, has_backlog)
    print(f"Placement eligible: {result['placement_eligible']}")
    print(f"Candidate category: {result['candidate_category']}")
