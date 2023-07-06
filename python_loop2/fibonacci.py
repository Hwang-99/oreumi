#1부터 n번째까지 직전에 입력 된 숫자와 현재 입력될 숫자를 작성

# sum = int(input())
# curr = 0
# next = 1
# for i in range(sum - 1):
#     curr, next = next, curr+next
# print(i)

# 변수 정의 및 입력

n = int(input())
curr = 0
next = 1

print(next)
#피보나치수열은 0+1부터 시작하기때문에 제외하고 3번째부터 출력하기위해서 (2,n+1)
for i in range (2,n+1):
    curr, next =next, curr + next

print(next)