#8. 자동판매기
Money = int(input("물건값을 입력하시오:"))
M1000 = int(input("1000원 지폐 개수:"))
M500 = int(input("500원 동전개수:"))
M100 = int(input("100원 동전개수:"))

MM = M1000 * 1000 + M500 * 500 + M100 * 100
MMM = MM - Money

P500 = MMM // 500
P100 = MMM % 500 // 100
P50 = MMM % 100 // 50 
P10 = MMM % 50//10
print("거스름돈: 500원=", P500 ,"100원=", P100 , "50원=" , P50 , "10원=" , P10)

#9. 주차장
Park = int(input("주차시간 입력:"))
Pay = Park // 15 * 2000
print("주차요금:", Pay)