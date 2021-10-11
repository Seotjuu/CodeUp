#1: 큰 수 반환 함수
a = int(input("첫 번째 정수를 입력하시오: "))
b = int(input("두 번째 정수를 입력하시오: "))

def get_max(a, b):
    if a > b:
        return a
    else:
        return b

A = get_max(20, 10)
print("큰 수는", A)

#2: 거리 반환 함수
x = int(input("x 좌표 입력: "))
y = int(input("y 좌표 입력: "))
import math

def distance():
    z = (x ** 2) + (y ** 2) 
    return z

print("거리: ", math.sqrt(distance()))

#3: 배수 찾기 함수
A = int(input("배수 입력: "))
B = int(input("최대값 입력: "))

def mul(n, max_num):
    if A >= B:
        print("잘못된 입력입니다.")
    else:
        for i in range(1, B + 1):
            x = A * i
            if x <= B:
                print(x)
mul(A, B)

#4: 햄버거 가게
def print_menu():
    print("1. 치즈버거 세트\n2. 불고기버거 세트\n3. 치킨버거 세트\n4. 종료")

print_menu()    
Menu = int(input("메뉴 선택: "))

def check_menu(a):
    if Menu == 1:
        print(Menu,"번 메뉴가 선택되었습니다.")
    elif Menu == 2:
        print(Menu,"번 메뉴가 선택되었습니다.")
    elif Menu == 3:
        print(Menu,"번 메뉴가 선택되었습니다.")
    elif Menu == 4:
        print("")
    else:
        print("잘못된 메뉴를 선택하셨습니다.")
check_menu(Menu)
