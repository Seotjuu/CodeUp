# 010-4740-7945
PhoneNum = input("전화번호를 입력하시오:")
LastNum1 = PhoneNum[9:14]
print("전화번호 끝자리는",LastNum1,"입니다")
a,b,LastNum2 = PhoneNum.split('-')
print("전화번호 끝자리는", LastNum2,"입니다")

# 010-4740-7945
Num = input("전화번호:")     
a,b,c = Num.split('-')
print(int(c[0]),int(c[0])*"#")
print(int(c[1]),int(c[1])*"#")       
print(int(c[2]),int(c[2])*"#")
print(int(c[3]),int(c[3])*"#")

# Ju Seok Lee
name = input("Enter name:") #영문으로 성이 뒤로 가게 적으시오.
o,t,T = name.split()
ID1 = o[0] + t[0] + T
ID2 = ID1.lower()
print("id:", ID2)

# 저는 파이썬프로그래밍을 아주 좋아합니다
TMI1 = input("문장:")
TMI2 = TMI1.replace(" ","")
ChongTMI = len(TMI2)
print("전체글자수:",ChongTMI)
Word1 = TMI1.split()
LEN1 = len(TMI2)
LEN2 = len(Word1)   
AVG1 = LEN1 / LEN2
AVG2 = round(AVG1,1)
print("평균글자수:",AVG2)

# 123456123456
Jumin = input("주민등록번호 앞 12자리 입력(하이픈 제외):")
Numx = int(Jumin[0]) * 2 + int(Jumin[1]) * 3 + int(Jumin[2]) * 4 + int(Jumin[3]) * 5
Numy = int(Jumin[4]) * 6 + int(Jumin[5]) * 7 + int(Jumin[6]) * 8 + int(Jumin[7]) * 9
Numz = int(Jumin[8]) * 2 + int(Jumin[9]) * 3 + int(Jumin[10]) * 4 + int(Jumin[11]) * 5
Num12 = Numx + Numy + Numz
Num13 = Num12 % 11
NumA = 11 - Num13
NumB = NumA % 10
print("맨 뒷자리:", NumB)

# 연세대
First = input("첫 번째 문장:")
Second = input("두 번째 문장:")
Third = input("세 번째 문장:")
Word_Plus = First[0] + Second[0] + Third[0]
print(Word)

# a
a = input("알파벳 소문자 입력:")
b = ord(a)
c = b + 3
Secret = chr(c)
print("암호:",Secret)