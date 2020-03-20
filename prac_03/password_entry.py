"""Zachary Keeffe"""
PASSWORD_LENGTH_MINIMUM = 4


def main():
    password = get_password()
    print(asterisk_conversion(password))


def asterisk_conversion(password):
    return "*" * len(password)


def get_password():
    password = input("Please enter a password: ")
    while len(password) < PASSWORD_LENGTH_MINIMUM:
        if len(password) < PASSWORD_LENGTH_MINIMUM:
            print("Insufficient Password Length.")
        password = input("Please enter a password: ")
    return password


main()
