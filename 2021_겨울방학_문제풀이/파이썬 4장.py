# 2021/01/18
a = input("오늘 날짜를 입력하시오:")
year, month, day = a.split("/")
print(year,"년",month,"월",day,"일")

# 77 88 100
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

# 홍길동 80 40000 0.20 0.09
Human = input("사원 이름을 입력하세요: ")
Hour = input("근무시간을 입력하세요: ")
Money = input("시간당 급여를 입력하세요: ")
Tax = input("원천징수세율을 입력하세요: ")
Jumin = input("주민세율을 입력하세요: ")
print( "\n","=" * 15)
print("* 사원 이름: {}".format(Human))
print("* 근무시간: {}시간".format(Hour))
print("* 시간당 급여: {}원".format(Money))
Hour_Money = int(Hour) * int(Money)
print("* 총 급여: {}원".format(Hour_Money))
Tax_Money = int(Hour_Money) * float(Tax)
Jumin_Money = int(Hour_Money) * float(Jumin)
t = Tax_Money + Jumin_Money
print("* 공제:\n  원천징수세 (0.20%): {}원\n  주민세 (0.09%): {}원\n  총 공제: {}원".format(Tax_Money, Jumin_Money, t))
s = Hour_Money - t
print("* 공제 후 급여: {}원".format(int(s)))

# 30000000
Year_Money = input("연 소득을 원 단위로 입력하시오:")
Year_Money = float(Year_Money)

if Year_Money <= 12000000:
    Tax = Year_Money * 0.06 - 0
elif Year_Money <= 46000000:
    Tax = Year_Money * 0.15 - 1080000
elif Year_Money <= 88000000: 
    Tax = Year_Money * 0.24 - 5220000
elif Year_Money <= 150000000:
    Tax = Year_Money * 0.35 - 14900000
elif Year_Money <= 300000000:
    Tax = Year_Money * 0.38 - 19400000
elif Year_Money <= 500000000:
    Tax = Year_Money * 0.40 - 25400000
else:
    Tax = Year_Money * 0.42 - 35400000
    
print("세금은 %d원입니다."%round(Tax,0))