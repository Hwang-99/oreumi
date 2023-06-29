# 1
a = [1, 2, 3, 4, 5]
b = []
for i in reversed(a):
    b.append(i)

print (b)

# 2
a = [1, 2, 3, 4, 5]

print(a[::-1])

# 3
a = [1, 2, 3, 4, 5]

left = 0
right = len(a) - 1
'''
len을 사용하는 이유
파이썬은 0번부터 시작하기때문에 전체 길이보다 -1을 해주어야함
'''

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1

print(a)

# 4
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# tuple test

a = (1, 2, [1, 2, 3])
a[2][2] = 1 # 3
print(a)

