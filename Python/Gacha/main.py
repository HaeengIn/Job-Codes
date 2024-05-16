import random as ran

student = ""
num = ""
restart = ""


def again():
    restart = input("Restart?(y/n) ")
    if restart == "y":
        run()
    if restart == "n":
        main()
    else:
        print("Invalid Input")
        
def run():
    while True:
        global student
        global num
        global restart
        if student == "":
            student = int(input("Last Number? "))
            num = ran.randint(1, student)
            print(num)
            again()
        if student != "":
            num = ran.randint(1, student)
            print(num)
            again()

def options():
    print("Fix / Back")
    b = input("")
    if b == "Fix":
        student = int(input("Fix Last Number: "))
        print("Last Number Fixed")
        main()
    if b == "Back":
        main()
    
def main():
    print("Start / Options / Exit")
    a = input()
    if a == "Start":
        run()
    if a == "Options":
        options()
    if a == "Exit":
        c = input("Exit Program?(y/n) ")
        if c == "y":
            print("Program Stopped")
            exit()
        if c == "n":
            main()
        else:
            print("Invalid Input")
    else:
        print("Invaild Input")
        
print("---Random Numbers---")
main()