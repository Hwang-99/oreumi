'''
반복문이란?
- 프로그램 내에서 똑같은 명령을 일정 횟수만큼 반복하여
수행하도록 제어하는 명령문

-for문과 while문이 있음

while: 반복 횟수가 명확하지 않을 때
for: 반복 횟수가 명확할 때
'''

# for문
# 문자열or리스트or튜플이 들어갔을 때 안에있는 요소를 하나씩 반복함
# 양식
# for 변수 in 문자열 (or 리스트 or 튜플):<--- 콜론
#     print(변수) <--- 들여쓰기

# for문 예시 1

list_food = ["햄버거","치킨","피자"] # <--- 1. 컴퓨터에서 먼저 읽음
for food in list_food: # <--- 2."햄버거" 4."치킨" 6."피자" 
    print(food) # <--- 3."햄버거" 5."치킨" 7."피자"
# 8.안에 있는 요소만큼 반복 후 for문 종료.
# 결과: 햄버거 치킨 피자

#for문 예시 2

hi = "안녕하세요"
for s in hi:
    print(s)
#결과: 안 녕 하 세 요

# while문
# 조건식이 True일 경우 실행문장 반복
# 양식
# while 조건식: <--- 콜론
#     실행문장 <--- 들여쓰기
#     실행문장 <--- 들여쓰기

# while문 예시

number = 1 # 1.
while number <= 3: # 2. 5. 8. 11.
    print(number) # 3. 6. .9
    number += 1 # <--- number = number + 1 # 4. 7. 10.

# while문 break - 반복문으 나가는 기능

while True:
    print("무한루프")
    break

# ---->

number = 1
while True:
    print(number)
    number += 1
    if number > 3:
        break