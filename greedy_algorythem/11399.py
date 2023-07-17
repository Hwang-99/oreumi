n = int(input())
peoples = list(map(int, input().split()))

peoples.sort()

total_time = 0

for i in range(1, n+1):
    total_time += sum(peoples[0:i])     # people[0:1] == people[0]

print(total_time)