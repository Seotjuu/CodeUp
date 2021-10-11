#1. 파티준비
Human = int(input("참석자의 수를 입력하시오: "))
Chicken = Human * 2
Beer = Human * 1
Cake = Human * 3
print("준비해야 할 치킨의 수: ", Chicken)
print("준비해야 할 맥주의 수: ", Beer)
print("준비해야 할 케익의 수: ", Cake,"\n")

#2. 변수값 교환
x = input("x를 입력하시오: ")
y = input("y를 입력하시오: ")
print("교환 전 = x:",x,"y:",y)
t = x
x = y
y = t
print("교환 후 = x:",x,"y:",y,"\n")

#3. 간단한 입출력과 계산 연습
Name = input("이름을 입력하시오:")
print(Name, "씨, 안녕하세요?\n파이썬에 오신 것을 환영합니다.")
int1 = input("첫 번째 정수를 입력하시오:")
int2 = input("두 번째 정수를 입력하시오:")
int3 = input("세 번째 정수를 입력하시오:")
sum = int1 + int2 + int3
print("세 정수의 합은 ",sum," 입니다.\n")

#4. 자동 입력 기사 쓰기
Stadium = input("경기장은 어디입니까?")
Win = input("이긴 국가는 어디입니까?")
Defeat = input("진 국가는 어디입니까?")
Mvp = input("우수 선수는 누구입니까?")
Score = input("스코어는 몇 대 몇입니까?")

print("\n========================================================\n오늘", Stadium,"에서 한일전 경기가 열렸습니다.")
print(Win,"과",Defeat,"은 치열한 공방전을 펼쳤습니다.")
print(Mvp,"이(가) 맹활약을 하였습니다.")
print("결국",Win,"이",Defeat,"을",Score,"로 이겼습니다.")
print("========================================================\n")

#5. 과일가게 판매가격 계산
Apple = 1500 / 2
Pear = 3000
Melon = 7000
Apple_Num = input("사과 갯수를 입력하세요:")
Pear_Num = input("배 갯수를 입력하세요:")
Melon_Num = input("멜론 갯수를 입력하세요:")
Sum = int(Apple * Apple_Num + Pear * Pear_Num + Melon * Melon_Num)
print("전체 금액은:",Sum)
print("\n")

#6. BMI 계산하기
Weight = float(input("몸무게를 kg 단위로 입력하시오:"))
Height = float(input("키를 미터 단위로 입력하시오:"))
Height_Power = float(Height ** 2)
Bmi = float(Weight / Height_Power)
print("당신의 BMi=",Bmi)
print("\n")

#7. 분초 계산하기
Sum = int(input("초 단위 시간을 입력하세요:",))
Minute = int(Sum / 60)
Second = int(Sum / 3600) % 60
Hour = int(Sum / 3600)
print(Hour,"시간",Minute,"분",Second,"초")
print("\n")
