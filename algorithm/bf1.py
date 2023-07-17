
from itertools import combinations
import sys

# N, M을 입력받는다 (N: 인원 수, M: 치킨 종류 개수)
N, M = map(int, input().split())

# 치킨 선호도 리스트
priority_list = []
for i in range(N): # 인원 수 N 만큼 실행
    priority_list.append(list(map(int,input().split()))) # 각 치킨에 대한 선호도


# ------------------------- 입력 부분

# 3가지 치킨을 선택하는 모든 경우의 수
# (0, 1, 2), (0, 1, 3), .....
comb = list(combinations(range(M), 3))

total_score_list = []
for i, j, k in comb:
    total_score = 0
    for l in range(N):
        max(priority_list[l][i], priority_list[l][j], priority_list[l][k])
    total_score_list.append(total_score)

print(max(total_score_list))