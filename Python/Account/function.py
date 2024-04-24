menu = "null"
id = "null"
password = "null"

def start():
    print("Login / SignUp")
    menu = input("Choose Menu: ")

def menu():
    if menu == "Login":
        login()
    if menu == "SignUp":
        signup()
    else:
        print("Invaild Input")

def signup():
    id = input("Enter New ID: ")
    password = input("Enter New Password: ")
    menu()

def login():
    login_id = input("Enter ID: ")
    login_password = input("Enter Password: ")