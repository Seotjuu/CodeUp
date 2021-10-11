# 12 5
Month = input("월을 입력하세요: ")
M = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print("{}월은{}입니다.".format(Month,M[int(Month) - 1 ]))                                                                                                                        

# December May
Month = input("월을 영어로 입력하세요: ")
M = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MM = M.index(Month)
print("{}은(는) {}월입니다.".format(Month,int(MM) + 1))

# 10 20 30 40 50
i1 = int(input("Enter 5 integers: "))
i2 = int(input("Enter 5 integers: "))
i3 = int(input("Enter 5 integers: "))
i4 = int(input("Enter 5 integers: "))
i5 = int(input("Enter 5 integers: "))
lll = [i1, i2, i3, i4, i5]
print("[{}, {}, {}, {}, {}]".format(i1, i2, i3, i4, i5))
Average1 = lll[0] + lll[1] + lll[2] + lll[3] + lll[4] 
Average2 = Average1 / 5
print("평균: %.1f" %Average2)
B = lll[0] * lll[0] + lll[1] * lll[1] + lll[2] * lll[2] + lll[3] * lll[3] + lll[4] * lll[4]
C = B / 5
D = Average2 * Average2
E = C - D
print("분산: %.1f" %E)

# 10 20 30 40 50
i1, i2, i3, i4, i5 = map(int, input("Enter 5 integers: ").split())
print("[{}, {}, {}, {}, {}]".format(i1, i2, i3, i4, i5))
Average1 = i1 + i2 + i3 + i4 + i5 
Average2 = Average1 / 5
print("평균: %.1f" %Average2)
B = i1 * i1 + i2 * i2 + i3 * i3 + i4 * i4 + i5 * i5
C = B / 5
D = Average2 * Average2
E = C - D
print("분산: %.1f" %E)

# 리스트 추가, 끼워넣기, 제거, 갯수세기, 정렬
Name = ["조용필","폴킴","황인욱"]
Name[len(Name):len(Name)] = ["청하"]
print("(1)=> {}".format(Name))
Name[2:2] = ["폴킴"]
print("(2)=> {}".format(Name))
Name1 = Name.count("폴킴")
print("(3)=> {}".format(Name1))
Name[3:4] = []
print("(4)=> {}".format(Name))
Name[1:2] = []
print("(5)=> {}".format(Name))
Name.sort(reverse=True)
print("(6)=> {}".format(Name))

# " "
Car = ["Gene", "Lex", "Infini", "Lambor", "Ferr"]
print("현재 차종: {}".format(Car))
Car[len(Car):len(Car)] = ["Merce"]
print("(1) Merce 차종 추가: {}".format(Car))
Car[1:2] = []
print("(2) Lex 차종 단종: {}".format(Car))
Car[5:5] = ["Gene-2020"]
print("(3) Gene 2020년형 추가: {}".format(Car))
Car1 = Car[1:4]
print("(4) 두 번째로부터 네 번째까지 개발한 모델: {}".format(Car1))

#7: 숫자 암호
A = input("암호 숫자를 5개 입력하시오: ")
a, b, c, d, e = A.split()
abcde = chr(int(a)) + chr(int(b)) + chr(int(c)) + chr(int(d)) + chr(int(e))
print(abcde)