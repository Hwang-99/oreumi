#개수 세기
n, x = map(int,(input().split()))
y = list(map(int, input().split()))
for num in y:
    if num < x:
        print(num)

