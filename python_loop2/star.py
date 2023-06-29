stars = int(input())

for star in range(1, stars+1):
    print("*" * star)

# ------> for문 두개 사용

# lines = int(input())

# for line in range(1, lines+1):
#     for i in range(line):
#         print("*", end = '') # end를 넣으면 자동개행 방지
#     # if line < lines:
#     print()

# 별찍기에서 end = "" 이 부분은 현재 속한 출력물을 다음
#  출력값과 이어지게 한다//  이 부분이 중요한 것 같습니다.

'''
lines = 5

        line    blank   star
*****   1       0       5
 ****   2       1       4
  ***   3       2       3
   **   4       3       2
    *   5       4       1       
'''