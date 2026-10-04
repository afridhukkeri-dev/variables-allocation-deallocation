def check_access(age, has_id, is_employee):
    if (age >= 18 and has_id is True) or is_employee is True:
        return "Access granted"
    return "Access denied"


if __name__ == "__main__":
    age = int(input("Enter age: "))
    has_id_input = input("Do you have an ID? (yes/no): ").strip().lower()
    has_id = has_id_input == "yes"
    is_employee_input = input("Are you an employee? (yes/no): ").strip().lower()
    is_employee = is_employee_input == "yes"
    print(check_access(age, has_id, is_employee))
