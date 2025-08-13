import re


pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9_]+'
pattern_password =r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}'
#pattern_password = r"^[0-9]+$"

def username_ok():
    while True:
        username = input("Enter username: ")
        # Username must contain at least one lowercase, one uppercase, one digit, and can include underscores
        if re.fullmatch(pattern, username):
            print("Username is valid.")
            return username
        else:
            print("Invalid username. It must contain at least one lowercase letter, one uppercase letter, one number, and can include underscores.")

def password_ok():
    while True:
        password = input("Enter password: ")
        # Password must be at least 8 characters, include one uppercase, one lowercase, one digit, and one special character
        if re.fullmatch(pattern_password, password):
            print("Password is strong.")
            return password
        else:
            print("Invalid password. It must be at least 8 characters long, include one uppercase letter, one lowercase letter, one number, and one special character.")

def register_account():
    username = username_ok()
    password = password_ok()
    print(f"Account registered successfully for username: {username}")


register_account()