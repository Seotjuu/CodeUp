#1: 냉장고 과일 관리하기
a = {"딸기", "바나나", "오렌지", "사과"}
b = "바나나" in a
print("냉장고에 바나나가 있는가?", b)
a.remove("바나나")
a.add("멜론")
print("바나나를 먹고 멜론을 사온 후 남은 과일?\n{}".format(set(a)))
print("남은 과일은 {}개".format(len(a)))

#2: 직원 관리
Member = {"다산", "길동", "민주", "순신", "보검", "중근", "대건", "수지", "세종"}
print("사원명단 {}".format(Member))
late = {"보검", "길동", "수지"}
print("지각자 명단 {}".format(late))
Absent = {"보검", "수지", "민주"}
print("결근자 명단 {}".format(Absent))
print("보너스 지급 대상자? {}".format(Member.difference(late,Absent)))
print("야근 대상자? {}".format(late.intersection(Absent)))
a = input("퇴사자는? ")
b, c = a.split()
d = input("신입사원? ")
Member.discard(b)
Member.discard(c)
Member.add(d)
print("새 사원명단 {}".format(Member))

#3: 장학금 수여
s = {"헨젤", "놀부", "길동", "심청", "흥부", "그레텔"}
print("학생 명단 {}".format(s))
Money1 = {"흥부", "길동", "헨젤"}
print("진리 장학금 수여 학생 명단 {}".format(Money1))
Money2 = {"심청", "흥부"}
print("자유 장학금 수여 학생 명단 {}".format(Money2))
Money12 = Money1 & Money2
print("이중 수혜 대상자 {}".format(Money12))
print("학교에 환원한 금액: {}원".format(len(Money12) * 5000000))

#4: 중복 단어 없애기 (This land is my land this land is your land)
Sentence = input("Enter Sentence:").split()
SS = set(Sentence)
S = " ".join(SS)
print(S)

#5 노래가사 단어 세기
Contents= "이슬비 내리는 이른 아침에 우산 셋이 나란히 걸어갑니다 파란 우산 빨간 우산 찢어진 우산 좁다란 학교 길에 우산 세 개가 이마를 마주 대고 걸어갑니다"
print("문장: {}".format(Contents))
Words = Contents.split()
dd = dict((k, Words.count(k)) for k in Words)
print("사용단어 딕셔너리: {}".format(dd))

#6: 제곱 딕셔너리
a =  input("정수 N을 입력하시오: ")
ii = {i:i**2 for i in range(int(a)+1)}
del ii[0]
print(ii)

#7: 2019년 전공의 모집 경쟁률
doctor1 = {"내과":103, "외과":92, "정형외과":173, "결핵과":0}
print("2019년 전공의 경쟁률(%): {}".format(doctor1))
doctor1.pop("결핵과")
doctor1.update({"예방의학과":133})
print("2019년 전공의 경쟁률(%): {}".format(doctor1))
doctor2 = ("내과", "정형외과", "예방의학과")
doctor2 = " ".join(doctor2)
print("경쟁률이 100% 이상인 전공: {}".format(doctor2))

#8: 두 자리수로 만들 수 있는 숫자
A1, A2 = map(int, input("정수 두 개를 입력하시오: ").split())
int_list1 = [A1, A2] 
B1, B2 = map(int, input("정수 두 개를 입력하시오: ").split())
int_list2 = [B1, B2] 
function_list = [(A1 * 10) + B1, (A1 * 10) + B2,(A2 * 10) + B1, (A2 * 10) + B2]
A = []
for v in function_list:
    if v not in A:
        A.append(v)
print(A)