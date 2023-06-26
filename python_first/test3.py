# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

input_text = input("")
A, B, C = input_text.split(" ")
A = (int(A))
B = (int(B))
C = (int(C))

print((A + B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)

# map 사용

A, B, C = map(int, input().split())

print((A + B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)