#1. 날짜 형식 변경
a = input("오늘 날짜를 입력하시오:")
year, month, day = a.split("/")
print("%s년 %s월 %s일"%(year,month,day))
print("{}년 {}월 {}일".format(year,month,day))
# %s를 쓰거나 format을 이용할 수도 있음

#2. 성적처리 출력
Scores = input("Scores: ")
f = "{:*^22}".format("Report")
print(f)

a,b,c = Scores.split()
History = "History:"
print(History + a.rjust(22-len(History)))
Mathematics = "Mathematics:"
print(Mathematics + b.rjust(22-len(Mathematics)))
Programming = "Programming:"
print(Programming + c.rjust(22-len(Programming)))

lll = "-" * 22
print(lll)
abc = int(a) + int(b) + int(c)
Total = "Total Score:"
print(Total + str(abc).rjust(22-len(Total)))
Average = "Average Score:"
A_S = abc / 3
print(Average + str(round(A_S)).rjust(22-len(Average)))
# 문자열 길이를 len으로 구함 -> 22에서 뺀만큼 오른쪽 정렬 해줌

#3. 급여명세서 출력
Human = input("사원 이름을 입력하세요: ")
Hour = input("근무시간을 입력하세요: ")
Money = input("시간당 급여를 입력하세요: ")
Tax = input("원천징수세율을 입력하세요: ")
Jumin = input("주민세율을 입력하세요: ")

print( "\n","=" * 15)
print("* 사원 이름: {}".format(Human))
print("* 근무시간: {}시간".format(Hour))
print("* 시간당 급여: {}원".format(Money))
gross = int(Hour) * int(Money)
print("* 총 급여: {}원".format(gross))
fedTax = int(gross) * float(Tax)
stateTax = int(gross) * float(Jumin)
totalDeduction = fedTax + stateTax
print("* 공제:\n  원천징수세 (0.20%): {}원\n  주민세 (0.09%): {}원\n  총 공제: {}원".format(fedTax, stateTax, totalDeduction))
net = gross - totalDeduction
print("* 공제 후 급여: {}원".format(int(net)))
# 변수 이름만 맞춰서 하면 됨!
# 나머지는 완벽하게 잘 한듯

#4. 세금 계산기
a = int(input('연 소득을 원 단위로 입력하시오: '))/1000000
print('세금은 {:,.0f}원입니다'.format(10000*(max(a-500,0)*42+max(min(a,500)-300,0)*40+max(min(a,300)-150,0)*38+max(min(a,150)-88,0)*35+max(min(a,88)-46,0)*24+max(min(a,46)-12,0)*15+min(a,12)*6)))
# if문 쓰지 않고 하는법
# max를 사용하면 됨. 한줄로 풀이를 줄일 수도 있음