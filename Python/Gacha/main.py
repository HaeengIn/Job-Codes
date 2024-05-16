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
        global student
        student = int(input("Fix Last Number: "))
        print("Last Number Fixed")
        main()
    if b == "Back":
        main()
    
def main():
    print("Start / Options / Exit / 한국어")
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
    if a == "한국어":
        main_kor()
    else:
        print("Invaild Input")

def again_kor():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        run_kor()
    if restart == "아니오":
        main_kor()
    else:
        print("잘못된 입력값입니다")

def run_kor():
    while True:
        global student
        global num
        global restart
        if student == "":
            student = int(input("마지막 번호를 입력해주세요: "))
            num = ran.randint(1, student)
            print(num)
            again_kor()
        if student != "":
            num = ran.randint(1, student)
            print(num)
            again_kor()

def options_kor():
    print("수정 / 뒤로가기")
    b = input("")
    if b == "수정":
        global student
        student = int(input("수정할 마지막 번호: "))
        print("수정되었습니다")
        main_kor()
    if b == "뒤로가기":
        main_kor()

def main_kor():
    print("시작 / 옵션 / 나가기 / English")
    a = input()
    if a == "시작":
        run_kor()
    if a == "옵션":
        options_kor()
    if a == "나가기":
        c = input("프로그램을 종료할까요?(예/아니오) ")
        if c == "예":
            print("종료되었습니다")
            exit()
        if c == "아니오":
            main_kor()
        else:
            print("잘못된 입력값임니다")
    if a == "English":
        main()
    else:
        print("잘못된 입력값임니다")

print("---Random Numbers---")
main()