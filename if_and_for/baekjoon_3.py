def MenOfPassion(A,n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum += A[i]*A[j]
    return sum

n = int(input())
print(n**2)
print(2)