#최대공약수와 최소공배수
# a, b =input("두 숫자를 입력:").split(" ")

# a = int(a)
# first_a = a
# b = int(b)
# first_b = b
# #형변환 필수!

# # a와 b는 b와 b를 a로 나눈 값의 나머지

# while b != 0:
#     a, b = b, a % b
# '''
# ex) a = 6, b = 4 일 때
# 첫번째로 식 실행 시 a = 4, b = 2
# 두번째로 식 실행 시 a = 2, b = 0
# b가 0이 되었으므로 반복문 종료 후 print
# '''
# print(f"최대공약수: {a}")
# print(f"최소공배수: {first_a * first_b / a}")

# #소인수분해

# 2, 3, 5, 7, 11 ,13, ...

# 30 = 2 * 15
# 30 = 2 * 3 * 5

n = int(input("소인수 분해 할 숫자를 입력해주세요!"))

factors = []
while n % 2 == 0:
    factors.append(2)
    n //= 2 # int

#n = 9
i = 3 # 3 = 홀수 중 제일 작은 소수

while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 2

#n이 1보다 클때만 실행
if n > 1:
    factors.append(n)

print(factors)

'''
ex)
10 = 1*10
10 = 2*5
10 = 3*3.3333.... <--- 나누어 지는 수가 이 이후로 작아짐 = 더이상 계산 필요 x (반환점)
10 = 4*2.5
10 = 5*2

10>= n*n
'''

