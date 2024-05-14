import random as ran

student = ""
num = ""
restart = ""


def again():
    restart = input("Restart?(y/n) ")
    if restart == "y":
        run()
    if restart == "n":
        print("Stopping Program...")
        exit()
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


run()
