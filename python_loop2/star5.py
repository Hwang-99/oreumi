# 별 찍기 - 5

# n = int(input())
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# #출력 (공백 * (n에서 i를 뺀 값) + "*" * (2i에서 1을 뺀 값)
# #왜 2i인가?
# # 찬혁아 예제를 좀 보자..

# n = int(input())
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for j in range(1, n)[::-1]:
#     print(" " * (n - j) + "*" * (2 * j - 1))

# 별 찍기 - 6

# n = int(input())
# for i in range(1, n + 1)[::-1]:
#     print(" " * (n - i) + "*" * (2 * i - 1))

# 별 찍기 - 7

# n = int(input())

# for i in range(1, n + 1):
#      print(" " * (n - i) + "*" * (2 * i - 1))
# for j in range(1, n)[::-1]:
#      print(" " * (n - j) + "*" * (2 * j - 1))


# 별 찍기 - 8

# n = int(input())

# for i in range(1, n + 1):
#      print("*" * (i) + 2*(" " * (n - i)) + "*" * (i))

# for j in range(1, n)[::-1]:
#      print("*" * (j) + 2*(" " * (n - j)) + "*" * (j))

# 별 찍기 - 9

# n = int(input())
# for i in range(1, n + 1)[::-1]:
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for j in range(2, n + 1):
#     print(" " * (n - j) + "*" * (2 * j - 1))

# 별 찍기 - 12

n = int(input())
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
for j in range(1, n + 1)[::-1]:
    print("0" * (n - j ) + "*" * (i - n))


