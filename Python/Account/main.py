menu = "null"
login_id = "null"
login_password = "null"
signup_id = "null"
signup_password = "null"

def menu():
    print("Login / SignUp")
    menu = print("Choose Menu: ")
    if menu == "SignUp":
        signup_id = input("Enter New ID: ")
        signup_password = input("Enter New Password")
        print("SignUp Complete!")
    if menu == "Login":
        login_id = input("Enter ID: ")
        login_password = input("Enter Password: ")
        if login_id == signup_id:
            print("Login Complete!")
            
print("---Make Your Account---")
menu()