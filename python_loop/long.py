"""
long = 4 byte
long * n = 4n byte
일때, 입력한 값을 byte로 나눠서 나온 값 만큼 long을 출력
"""

#byte를 정의 - 숫자열
#long은 4 byte

# byte = 4
# long = byte // 4

sum = input()
for i in range(int(sum) // 4):

#4로 나눈 long의 값 만큼 "long "을 출력 후(공백), 끝에 "int"

    print("long ", end='')
print("int")
#long을 