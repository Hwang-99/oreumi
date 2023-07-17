import sys

N = int(sys.stdin.readline())

time = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time.append([s, e])

### -------------------------------------- 입력

time.sort(key=lambda x:(x[1], x[0]))


count = 0
end_time = 0

for i in range(N):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)