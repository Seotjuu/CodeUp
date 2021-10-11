#1. 인터넷 쇼핑몰
# 정답

# 고급) 수학을 이용하는방법
# M -= (M>=100000) * M * 0.05
# M이 100000보다 크면 (M>=100000)이 1이 되니까 빼고, 아니면 0이니까 안뺌

#2. 수하물 비용 계산
# 정답

#3. 큰 수 출력
# 정답

# 4. 팩토리얼 계산
# 정답

# 고급) 재귀함수를 이용하는 방법
# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n이 1보다 작으면 1팩토리얼 = 1을 출력
# 나머지는 n에 (n-1)! 을 출력해주면 알아서 여러번 함수를 돌면서 계속 곱한 값을 출력

#5. 숫자 세기
# 정답

# for문을 이용하는 방법
# a = int(input("a를 입력하시오: "))
# b = int(input("b를 입력하시오: "))
# for i in range(a,b+1):
#     print("count", i)

#6. 색깔별 우산
# 정답

#8. 평균 날씨 구하기
# average = sum(weather.values())/len(weather)
# 이런 식으로 weather.values 를 이용해 바로 가져와도 됨
# 굳이 list로 변환 안하고

#9. 숫자 반복 덧셈
i1 = 0
i2 = input("숫자를 입력하시오: ")
while i2 != "yonsei":
    i1 += int(i2)
    i2 = input("숫자를 입력하시오: ")

# 위처럼 하면 굳이 while True와 break를 사용할 필요 없음

#HW1. 5를 제외한 숫자 반복 덧셈
i1 = 0
i2 = input("숫자를 입력하시오: ")
while i2 != "yonsei":
    if '5' not in i2:
        i1 += int(i2)
    i2 = input("숫자를 입력하시오: ")

# 위처럼 하면 continue와 break을 둘 다 사용할 필요 없음

#HW2. 소수의 개수 구하기
# 정답
# 꼭 여러번씩 보면서 이해해봐