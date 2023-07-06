a = 2
b = 1
print(a, b)
temp = a
#a라는 곳을 다른 곳에 저장

a = b # 2 1
b = temp # 1 2
print(a, b)

a = 2
b = 1
print(a, b)
a, b = b, a
print(a, b)

