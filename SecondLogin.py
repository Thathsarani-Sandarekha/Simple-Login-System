user_details = "User Details.txt"


def get_existing_users():
    with open("r", user_details) as ud:
        for line in ud.readline():
            username, password = line.split()
            yield username, password


def is_authorized(username, password):
    return any((user == (username, password) for user in get_existing_users()))


def user_exists(username):
    return any((usr_name == username) for usr_name in get_existing_users())


def ask_user_credentials():
    print("please provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    return name, password


def check_details():
    name, password = ask_user_credentials()
    if is_authorized(name, password):
        return "Welcome back" + name
    if user_exists(name):
        return "Password entered is wrong"
    return "Name not found. please sign up."


def get_details():
    name, password = ask_user_credentials()
    if not user_exists(name):
        return "Name Unavailable. please try again"


get_existing_users()
is_authorized()