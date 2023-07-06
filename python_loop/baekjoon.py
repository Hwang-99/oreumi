#소인수분해(소수로만 수를 나누기)
n = int(input())  # 사용자로부터 입력 받기

factors = []  # 소인수를 저장할 리스트

# 2로 나누어 떨어질 때까지 반복
while n % 2 == 0:
    factors.append(2)  # 2를 factors 리스트에 추가
    n //= 2  # n을 2로 나누기

# n (예: 36의 경우 몫은 9가 됨)

i = 3  # 3부터 소인수를 검사하기 시작

# i가 n의 제곱근보다 작거나 같을 때까지 반복
while i * i <= n:

    # i로 나누어 떨어질 때까지 반복
    while n % i == 0:
        factors.append(i)  # i를 factors 리스트에 추가
        n //= i  # n을 i로 나누기
    i += 2  # 소인수를 검사하기 위해 i를 2씩 증가시킴, 위 while문에서 짝수는 모두 해결.

if n>1:
    factors.append(n)#마지막으로 남은 값도 추가
print(factors)

price = int(input())  # 상품의 가격을 입력받음
amount = int(input())  # 주문한 상품의 수량을 입력받음
total_price = 0  # 주문한 상품들의 총 가격을 초기화

for i in range(amount):
    a_prc, b_amt = map(int, input().split())  # 상품 가격과 수량을 입력받음
    total_price += a_prc * b_amt  # 상품 가격과 수량을 곱하여 총 가격에 더함

if total_price == price:
    print("Yes")  # 총 가격이 입력받은 가격과 일치하면 "Yes" 출력
else:
    print("No")  # 총 가격이 입력받은 가격과 일치하지 않으면 "No" 출력