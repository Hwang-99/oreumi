# score_list = [90, 45, 70, 60, 55]
# number = 1
# for score in score_list:
#     print(score)
#     if score >= 60:
#         result = "합격"
#     else:
#         result = "불합격"
#     print("{}번 학생은 {} 입니다.".format(number, result))
#     number += 1

# number = 0
# while number <13:
#     print("파이썬 최고!")
#     number += 1

while True:
    num1 = int(input("첫 번째 정수 입력 >> "))
    num2 = int(input("두 번째 정수 입력 >> "))

    if num1+num2 == 0:
        break

    print("두 수의 합 : {}".format(num1+num2))
print("프로그램이 종료되었습니다.")