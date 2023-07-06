# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.


n = int(input(""))

sum = 0
for i in range(0, n + 1): # <--- 숫자를 반복 해야함. range로 시작점 잡기
    sum += i # <--- i까지의 모든 값 더해주기

print(sum)

