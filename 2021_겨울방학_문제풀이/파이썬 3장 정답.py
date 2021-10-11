#1. 핸드폰 끝번호 출력
PhoneNum = input("전화번호를 입력하시오:")
LastNum11 = PhoneNum[9:13:1]
LastNum12 = PhoneNum[9:]
LastNum13 = PhoneNum[-4:]
# 인덱싱 [처음:끝:간격]
# 처음 <= x < 간격
# 간격이 생략되면 1, 끝이 생략되면 맨 끝까지, 처음이 생략되면 처음부터
# -4처럼 음수가 들어가면 뒤에서 4번째부터 끝까지
print("전화번호 끝자리는",LastNum11,"입니다")
print("전화번호 끝자리는",LastNum12,"입니다")
print("전화번호 끝자리는",LastNum13,"입니다")
LastNum2 = PhoneNum.split('-')[2]
print("전화번호 끝자리는", LastNum2,"입니다")
# split을 하면 배열이 나옴.
# '-'를 통해 나뉘는게 3개니까 길이 3짜리 배열이 나오고 그 중 2번 인덱스 (세번째) 요소를 뽑는 것
# 물론 a,b,LastNum2 로 출력을 받아도 됨.
# 그렇게 여러 변수에 List를 바로 입력하는 것도 가능.

#2. 전화번호 분리하여 출력 
Num = input("전화번호:")     
a,b,c = Num.split('-')
print(int(c[0]),int(c[0])*"#")
print(int(c[1]),int(c[1])*"#")       
print(int(c[2]),int(c[2])*"#")
print(int(c[3]),int(c[3])*"#")

#3. 계정 id 자동 생성
name = input("Enter name:")
o,t,T = name.split()
ID1 = o[0] + t[0] + T
ID2 = ID1.lower()
print("id:", ID2)

#4. 문장 단어 분석하기
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
# Len1 = sum([len(x) for x in Word1.split()])
# 이렇게 해주면 split된 요소들의 각각의 길이의 배열을 구하고
# 그 배열의 sum을 구해 전체 길이를 구할 수도 있음
# Len1 = len(TMI1)-TMI1.count(' ')
# 이렇게 해주면 전체 길이에서 빈칸의 길이를 빼서 글자수를 체크할 수도 있음.

# 5. 주민등록번호
Jumin = input("주민등록번호 앞 12자리 입력(하이픈 제외):")
Numx = int(Jumin[0]) * 2 + int(Jumin[1]) * 3 + int(Jumin[2]) * 4 + int(Jumin[3]) * 5
Numy = int(Jumin[4]) * 6 + int(Jumin[5]) * 7 + int(Jumin[6]) * 8 + int(Jumin[7]) * 9
Numz = int(Jumin[8]) * 2 + int(Jumin[9]) * 3 + int(Jumin[10]) * 4 + int(Jumin[11]) * 5
Num12 = Numx + Numy + Numz
Num13 = Num12 % 11
NumA = 11 - Num13
NumB = NumA % 10
print("맨 뒷자리:", NumB)
