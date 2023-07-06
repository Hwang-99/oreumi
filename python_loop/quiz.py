def calculate_average(n):
    total = 0
    count = 0
    for i in range(1, n+1):
        total += i
        count += 1
    average = total / count
    return average

n = int(input("n을 입력하세요: "))
result = calculate_average(n)
print("평균:", result)