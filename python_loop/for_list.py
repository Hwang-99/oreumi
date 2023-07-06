# 과일 출력 

# fruits = ["사과", "수박", "배"]
# for x in fruits:
#     print(x)

# range
# for i in range (1, 101):
#     print(i)

# fruits = ["사과", "수박", "배"]
# prices = [2500, 15000, 5000]
# for idx, x in enumerate(fruits):
#     print(idx+1,x)


# fruits = ["사과", "수박", "배"]
# prices = [2500, 15000, 5000]
# amounts = [5, 6, 3]
# for fruit, price, amount in zip(fruits, prices, amounts):
#     profit = price * amount
#     print(fruit, price, amount, profit)

# for i in range(0, 10):
#     if i == 5:
#         break
#     print(i)

# for i in reversed(range(0,10)):
#     print(i)

# a = ["사과","수박","배"]
# for i in reversed(a):
#     print(i)

# with open("test.txt", "r", encoding="utf-8") as f:
#     text = f.read().split('\n')
#     for idx, line in enumerate(text):
#         name, score = line.split(" ")
#         print(f'{idx+1}번째 학생: {name}, 점수: {score}')

# 많은 항목 중 오류 찾기
# for i in range(0, 10000):
#     if i == 6000:
#         print(i)
#     print(i)

#enumerate : for 다음에 작성
# test=["1","2"]
# for idx, i in enumerate(test):
#     print(f'{idx}번째')

# a = "Hello World!"
# cnt = 0
# for i in a:
#     cnt+=1
# print(cnt)

# a = ["1", "2", "3", "4", "5"]
# sum = 0
# for i in a:
#     sum+= int(i)
# print(sum)

# a = "지금 나오는 a는 몇번째일까요?"
# print(a[0:2])

# a = input("팩토리얼 입력:")
# factorial = 1
# for i in range(1,int(a)+1):
#     factorial *= i
# print(factorial)

# a = int(input (""))

# for i in range(1, 10):
#     result = a * i
#     print(f"{a} * {i} = {result}")

a = int(input(""))

for i in range(1, a+1):
    b, c = input("").split(" ")
    print(int(b) + int(c))
#숫자를 input값만큼 받고 두 숫자를 쪼개서 더하기