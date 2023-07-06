# 1330 숫자 크기 비교

# a, b = map(int,input().split())

# if a == b:
#     print("==")
# elif a < b:
#     print("<")
# elif a > b:
#     print(">")
# else:
#     print("Type Error")


# 9498 시험 성적

# n = int(input())

# if 90 <= n :
#     print("A")
# elif 80 <= n :
#     print("B")
# elif 70 <= n :
#     print("C")
# elif 60 <= n :
#     print("D")
# else:
#     print("F")


# 2753 윤년 계산
# 1: 윤년 0: 윤년아님

# n = int(input())

# if n % 400 == 0: 
#     print("1")
# else:
#     if n % 100 == 0:
#         print("0")
#     else:
#         if n % 4 == 0:
#             print("1")
#         else:
#             print("0")

# 14681 사분면 고르기

x = int(input())
y = int(input())

if x > 0 and y > 0 :
    print("1")
elif x < 0 and y > 0 :
    print("2")
elif x < 0 and y < 0 :
    print("3")
elif x > 0 and y < 0 :
    print("4")
else :
    print("TYPE ERROR")    