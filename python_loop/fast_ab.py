import sys
sum = sys.stdin.readline().rstrip()

for i in range(int(sum)):
    a = sys.stdin.readline().rstrip().split(" ")
    print(int(a[0])+int(a[1]))



# n을 입력하면 n만큼 a+b를 연산해주고, 결과값을 출력