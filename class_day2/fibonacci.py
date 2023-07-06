# n = int(input())

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

if n < 0:
    print("n은 음수일 수 없습니다.")
else:
    result = fibonacci(n)
    print(result)
    
