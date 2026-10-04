required_skills = ["python", "sql", "git", "html"]


def check_skill(skill_name):
    skill = skill_name.lower()
    if skill in required_skills:
        return "Skill available"
    return "Skill not available"


if __name__ == "__main__":
    skill = input("Enter skill name: ")
    print(check_skill(skill))
