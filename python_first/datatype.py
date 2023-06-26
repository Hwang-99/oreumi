# None
print(type(None))

# Bool
print(type(True))
print(type(False))

# 숫자형
print(type(5)) # 정수 int
print(type(3.14)) # 실수 float
print(type(2 + 3j)) # 복소수 complex

# 문자형 str
print (type("예시"))

# 시퀀스 - 자료형
print(type((1, 2, 4))) # 소괄호 tuple
print(type([1, 2, 4])) # 대괄호 list

# dict
print(type({"A":10, "B":20}))

# set
print(type({"1", "2", "3"}))

# function
def f():
    return 1
print(type(f))

a = 2 # int
print(type(str(a)))