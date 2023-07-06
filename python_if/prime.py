n = int(input())

is_prime = True # 소수 판별 플래그값

'''
17
= 2 * 8.5
= 3 * 5.xx ...
= 4 * 4.25

17**0.5 = 4.066
= int(4.066) = 4
'''
'''
17 = 4
19 = 4
26 = 5
8 = 2
11 = 3
'''

# for i in range(2, int(n**0.5) + 1): # n**0.5 == √n

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime: # '' == True
    print("소수이다!")
else:
    print("소수가 아님!")
'''
1. 소수를 판별했을때 True이면 소수이다

2. 만약에 소수가 아닌 경우
2-1. i로 나누어 떨어지는 경우가 있으면 소수가 아님.

is_prime = False
'''