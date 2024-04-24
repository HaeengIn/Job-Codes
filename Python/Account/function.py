def menu():
    signup_id = "null"
    signup_password = "null"
    login_id = "null"
    login_password = "null"

    print("Login / SignUp")
    choose = input("Choose Menu: ")
    if choose == "Login":
        login()
    if choose == "SignUp":
        signup()
    else:
        print("Invaild Input")

def signup():
    signup_id = input("Enter New ID: ")
    if signup_id == login_id:
        print("This ID already exists.")
    else:
        login_id = signup_id
        signup_password = input("Enter New Password: ")
        login_password = signup_password

def login():
    login_id = input("Enter ID: ")
    login_password = input("Enter Password: ")