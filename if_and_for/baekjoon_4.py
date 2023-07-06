def MenOfPassion(A,n):
    sum = 0
    for i in range(n - 1):
        for j in range (i + 1, n):
            sum += A[i] * A[j] # 코드 1
    return sum

n = int(input())
print(n*(n-1) // 2)
print(2)