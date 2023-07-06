# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

def outer_function():

    x = 10 #2번 실행

    def inner_function():
        print(x) #4번 실행

    inner_function() # 3번 실행


outer_function() # 1번 실행