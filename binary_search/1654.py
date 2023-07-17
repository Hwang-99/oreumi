import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

start, end = 1, max(lan)


# start가 end보다 꺼질 때 종료
# while문을 벗어나기 위해서는 start와 end가 교차
# 최대값을 구하는 문제는 end, 최소값은 start
while start <= end:

    mid = (start + end) // 2
#------------------------조건이--------------------
    total_count = 0

    # 총 만든 랜선의 개수
    for length in lan:
        total_count += (length // mid)
#-----------------------중요함---------------------

    # 무한루프에 빠지지 않기 위해 각 +1, -1 해줌
    # mid가 계속 움직이면서 start와 end가 교차되기 위해
    if total_count >= N:
        start = mid + 1
    
    else:
        end = mid - 1

# 해당 값을 구하고 싶다면 end 출력
print(end)