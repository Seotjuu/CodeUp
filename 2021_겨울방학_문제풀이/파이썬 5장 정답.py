#1. 영문 월 이름 출력하기
Month = input("월을 입력하세요: ")
M = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("{}월은{}입니다.".format(Month,M[int(Month) - 1 ]))

#2. 영문 월 이름 출력하기
Month = input("월을 영어로 입력하세요: ")
M = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MM = M.index(Month)
print("{}은(는) {}월입니다.".format(Month,MM + 1))
# index는 어차피 int라 int로 바꿔줄 필요 없음

#3. 리스트 연습
lll = []
for i in range(5):
	n = int(input("Enter 5 integers: "))
	lll.append(n)
	# 배열.append(요소) : 배열 끝에 요소 삽입
	# 배열.insert(인덱스,요소) : 배열의 인덱스 번째에 요소 삽입
# for문 연습해봐. for랑 if문만 잘써도 할 수 있는 거 많다.

print(lll)
# format 써줄 필요 없음. 리스트는 대괄호 안에서 자동으로 출력됨

Average = sum(lll) / 5
print("평균: %.1f" %Average)
# 더하는 건 sum써주면 됨.

B = 0
for x in lll:
	B = B + x**2
	# B += x**2 해도 됨
C = B / 5
D = Average * Average
E = C - D
print("분산: %.1f" %E)

#4. 리스트 연습
lll = map(int, input("Enter 5 integers: ").split())
lll = list(lll)
# map쓴건 아주 잘했음.
# 근데 그냥 그대로 리스트 안에 넣어주면 바로 리스트로 들어감
# i1, i2, ... 이렇게 넣을 필요가 없다는 거지.
# 배열 잘 활용하는게 프로그래밍의 기본이니까 잘 익혀둬.

print(lll)
Average = sum(lll) / 5
print("평균: %.1f" %Average)

B = 0
for x in lll:
	B = B + x**2
C = B / 5
D = Average * Average
E = C - D
print("분산: %.1f" %E)

#5. 리스트 메소드 연습
Name = ["조용필","폴킴","황인욱"]
# Name[len(Name):len(Name)] = ["청하"]
Name.append("청하")
# 배열[a:b:c] a보다 크거나 같고, b보다 작은 인덱스를 c간격으로
# c가 생략되면 c = 1
# a가 생략되면 a = 0
# b가 생략되면 b = 배열 길이 (배열끝)
print("(1)=> {}".format(Name))
# Name[2:2] = ["폴킴"]
Name.insert(2,"폴킴")
print("(2)=> {}".format(Name))
Name1 = Name.count("폴킴")
print("(3)=> {}".format(Name1))
# Name[3:4] = []
Name.remove("황인욱")
# 배열.remove(요소)
print("(4)=> {}".format(Name))
# Name[1:2] = []
Name.pop(1)
# Name.remove(Name[1])
# del Name[1]
# 배열.pop(인덱스)
# 배열.remove(배열[인덱스]) 해도 됨
# del 배열[인덱스] 해도 됨
print("(5)=> {}".format(Name))
Name.sort(reverse=True)
print("(6)=> {}".format(Name))

#6. 자동차 회사
Car = ["Gene", "Lex", "Infini", "Lambor", "Ferr"]
print("현재 차종: ",Car)
Car.append("Merce")
print("(1) Merce 차종 추가: "Car)
Car.remove("Lex")
print("(2) Lex 차종 단종: "Car)
Car.append("Gene-2020")
print("(3) Gene 2020년형 추가: "Car)
Car1 = Car[1:4]
print("(4) 두 번째로부터 네 번째까지 개발한 모델: ",Car1)
# 굳이 print에서 format을 매번 써줄 필요 없음
# 사실 그냥 콤마로 구분해주면 알아서 print됨

#7. 숫자 암호
A = input("암호 숫자를 5개 입력하시오: ").split()
# split해주면 A에 배열로 들어감
abcde = ''
# 빈 문자열 선언해주고 for문 돌리면서 거기에 하나씩 추가할거임
for x in A:
	abcde = abcde + chr(int(x))
	# abcde += chr(int(x))
print(abcde)