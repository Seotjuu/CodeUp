#1. 냉장고 과일 관리하기
# 정답

#2. 직원 관리
# difference, intersection 쓴것 잘했음.
# 정답

#3. 장학금 수여
# 정답

#4. 중복 단어 없애기
# 정답

#5. 노래가사 단어 세기
# 정답

# dd = dict((k, Words.count(k)) for k in Words)
# 이 문장 잘 기억해둬 쓸일 많을거임
# for문을 뒤에 넣어서 자연스럽게 배열 만드는 거

# *의 기능 = 리스트 깨기
# a = [[1,2],[3,4],[5,6]]
# print(list(zip(*a)))

# def pprint(x):
#     print("\n",'*'*20,"\n",x)

# pprint("1. 리스트")
# my_list = ["one","two","three","four","five","five"]
# print("0번째 요소 : ",my_list[0]) # 어떤 value를 가져오기 위해서는 index(순서)입력

# pprint("2. 딕셔너리")
# my_dict = {"one":1,"two":2,"three":3,"four":4,"five":5}
# my_dict = {x:i+1 for i,x in enumerate(my_list)}
# # 둘 다 같은 말

# my_dict["one"] = 2 # value 수정 가능
# print(my_dict.items()) # (key,value) 값이 전부 출력
# print(my_dict.keys()) # key(이름) 만 출력
# print(my_dict.values()) # value 만 출력
# print("one이란 key를 가진 value : ",my_dict["one"]) # 어떤 value를 가져오기 위해서는 key값 입력

# pprint("3. 셋(집합)")
# my_set1 = set(my_list) # 중복되는 five는 하나 빠짐
# my_set1 = {*my_list}
# # 둘 다 같은 말
# my_set2 = {"one","seven","eight","two"}
# # set에는 숨겨진 key값이 존재함.
# # set은 개별 요소를 가져올 수 없음. 가져오려면 다른 배열로 바꿔줘야함.

# print("교집합 : ",my_set1&my_set2)
# print("교집합 : ",my_set1.intersection(my_set2))

# print("합집합 : ",my_set1|my_set2)
# print("합집합 : ",my_set1.union(my_set2))

# print("차집합 : ",my_set1-my_set2)
# print("차집합 : ",my_set1.difference(my_set2))

# pprint("4. 튜플(순서쌍)")
# my_tuple = ((1,5),(2,10))
# print(my_tuple[0]) # 어떤 value를 가져오기 위해서는 index입력
# print(my_tuple[0][0])

# pprint("5. 튜플과 딕셔너리의 응용")
# my_dict = {x:y for x,y in my_tuple}
# print(my_dict)
# # 이런 식으로 tuple은 리스트에 비해 자료를 꺼내오는 것이 자유로움
# # 리스트는 가장 간단하고 쉽지만 사실상 효율성이 가장 떨어짐

#6. 제곱 딕셔너리
# 정답
# ii = {i:i**2 for i in range(1,int(a)+1)}
# 위처럼 하면 굳이 del ii[0]을 할 필요가 없음

#7. 2019년 전공의 모집 경쟁률
# doctor1["예방의학과"] = 133
# 딕셔너리[키] = 밸류
# 이렇게 해주는게 더 빠르고 간단함
# 
# (1)
# doctor2 = ''
# for key in doctor1.keys():
#     if docter1[key] > 100:
#         doctor2 += key
# 
# (2)
# doctor2 = ''
# for key,value in doctor1.items():
#     if value > 100:
#         doctor2 += key
# 
# for문과 if문을 적절히 섞어야함.
# 딕셔너리.keys()하면 key만 출력, .items()하면 key,value의 순서쌍이 출력

#8. 두 자리수로 만들 수 있는 숫자
A = input("정수 두 개를 입력하시오: ").split()
B = input("정수 두 개를 입력하시오: ").split()
# map int는 잘 썼는데 굳이 먼저 쓸 필요 없이 문자열로 합해준 다음에 int로 바꾸면 됨
function_list = []
for a in A:
    for b in B:
        v = int(a+b)
        if v not in function_list:
            function_list.append(v)
            # a+b하면 문자열이 바로 합쳐짐
            # 그걸 int안에 넣으면 10의자리, 1의자리로 들어감
function_list.sort()
print(function_list)