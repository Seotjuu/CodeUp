#1. 출력
print('Hello world!')

#2. 변수
x = 2020
print(x)

#3. 자료형
a = str(2020)
print(int(a)+1) # int 형태로 형변환 한 뒤 1 추가
print(a*2) # str 형태 두 개를 붙여서 출력
print(int(a)*2) # int 형태로 형변환 한 뒤 2배하여 출력

#4. 같음 다름
a = 1
b = 2
if a != b:
	print("같지 않다.")
else:
	print("같다.")

if a == b:
	print("같다.")
else:
	print("같지 않다.")

a = "1"
b = 1
if type(a) == type(b):
	print("유형이 같다.")
else:
	print("유형이 같지 않다.")