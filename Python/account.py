login_id = ""
login_password = ""
signup_id = ""
signup_password = ""

def menu():
    print("Login / SignUp")
    menu = input("Choose Menu: ")
    if menu == "SignUp":
        signup_id = input("Enter New ID: ")
        signup_password = input("Enter New Password")
        print("SignUp Complete!")
    if menu == "Login":
        login_id = input("Enter ID: ")
        login_password = input("Enter Password: ")
        if login_id == signup_id:
            print("Login Complete!")
            menu()
        if login_id != signup_id:
            print("Incorrect ID!")
print("---Make Your Account---")
menu()