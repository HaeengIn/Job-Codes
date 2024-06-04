# random 함수 임포트
import random as ran

# 변수 선언
student = ""
num = ""
restart = ""

# Invaild Input 출력
def invalid():
    print("Invalid Input")

# 다시 뽑기 실행
def again():
    restart = input("Restart?(y/n) ")
    if restart == "y":
        run()
    if restart == "n":
        main()
    else:
        invalid()
        again()

# 메인 실행
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
            invalid()
    if a == "한국어":
        main_kor()
    else:
        invalid()
    
# 랜덤 뽑기 실행
def run():
    while True:
        global student
        global num
        global restart
        if student == "":
            student = int(input("Last Number? "))
            num = ran.randint(1, int(student))
            print("Picked Number:", num)
            again()
        if student != "":
            num = ran.randint(1, student)
            print("Picked Number:", num)
            again()

# 옵션 실행
def options():
    print("Fix / Current / Back")
    b = input("")
    if b == "Fix":
        global student
        student = int(input("Fix Last Number: "))
        print("Last Number Fixed")
        options()
    if b == "Current":
        if student == "":
            print("Last Number Is Not Set")
            options()

# 다시 뽑기 실행
def again_kor():
    restart = input("다시 뽑을까요?(예/아니오) ")
    if restart == "예":
        run_kor()
    if restart == "아니오":
        main_kor()
    else:
        print("잘못된 입력값입니다")

# 랜덤 뽑기 실행
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

# 옵션 실행행
def options_kor():
    print("수정 / 현황 / 뒤로가기")
    b = input("")
    if b == "수정":
        global student
        student = int(input("수정할 마지막 번호: "))
        print("수정되었습니다")
        options_kor()
    if b == "현황":
        if student == "":
            print("마지막 번호가 설정되어 있지 않습니다.")
            options_kor()
        if student != "":
            print("현재 설정된 마지막 번호:", student)
            options_kor()
    if b == "뒤로가기":
        main_kor()

# 메인 실행
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

# 메인 실행
print("---Random Numbers---")
main()