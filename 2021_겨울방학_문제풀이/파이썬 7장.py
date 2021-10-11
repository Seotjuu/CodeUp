#1: 인터넷 쇼핑몰
M = int(input("구입 금액을 입력하시오:"))
if M >= 100000:

    MM = M * 0.05
    print("지불 금액은 {}원입니다.".format(int(M - MM)))
else:
    print("지불 금액은 {}원입니다.".format(M))

#2: 수하물 비용 계산
Kg = int(input("짐의 무게는 얼마입니까? "))

if Kg >= 20:
    print("무거운 짐은 20000원을 내셔야 합니다.\n감사합니다.")
else:
    print("짐에 대한 수수료는 없습니다.\n감사합니다.")

#3: 큰 수 출력
A = int(input("첫 번째 정수: "))
B = int(input("두 번째 정수: "))
if  A > B:
    print("큰 수는 {}".format(A))
else:
    print("큰 수는 {}".format(B))

#4: 팩토리얼 계산
f = 1
i = int(input("정수를 입력하시오: "))
for N in range (1, i + 1):
    f = f * N

print("{}! = {}".format(i,f))

#5: 숫자 세기
a = int(input("a를 입력하시오: "))
b = int(input("b를 입력하시오: "))
A = a - 1
while A < b:
    A = A + 1
    print("Count ", A)

#6: 색깔별 우산
Rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

for Color in Rainbow:
    print(Color + " umbrella")

#8: 평균 날씨 구하기
weather = {'10 월 1 일 ': 24, '10 월 2 일 ': 22, '10 월 3 일 ': 23, '10 월 4 일 ': 22, '10 월 5 일 ': 18}
b = []
for a in weather:
    b.append(weather [a])

average = sum(b)/len(b)
print("10월 1일부터 10월 5일까지 최고 온도의 평균은 {}".format(average))

#9: 숫자 반복 덧셈
i1 = 0
while True:
    i2 = input("숫자를 입력하시오: ")
    if i2 == "yonsei":   
        break 
    i1 += int(i2)

print("모두 더한 값은 ", i1)

#HW 1: 5를 제외한 숫자 반복 덧셈
i1 = 0
while True:
    i2 = input("숫자를 입력하시오: ")
    if '5' in i2:
        continue
    if i2 == "yonsei":   
        break 
    i1 += int(i2)
    

print("모두 더한 값은 ", i1)

#HW 2: 소수의 개수 구하기
B = int(input("숫자를 입력하시오: "))
A = list(range(2,B+1))
for i in range(2, B+1):
    for j in range(2, i):
        if i % j == 0:
            A.remove(i)
            break
print(A)
print(B, "이하의 소수의 개수는 ", len(A))