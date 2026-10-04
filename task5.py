def validate_user(username, password):
    if username == "admin" and password == "python":
        return "Valid user"
    return "Invalid user"


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(validate_user(username, password))
