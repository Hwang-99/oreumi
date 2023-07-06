# star = int(input())
# for i in range(1, star+1):
#     for j in range(star-i):
#         print(' ', end='')
#     for k in range(i):
#         print("*", end='')
#     print()

lines = int(input())

    #줄 생성, lines로 작성을 해도 문제없으나 가독성 위해 1, lines + 1 사용
for line in range(1, lines + 1):

    #공백 생성 blank = lines - line
    for blank in range(lines-line):
        print(" ", end='')
    #별 생성
    for star in range(line):
        print("*", end='')
    #마지막 줄바꿈 제거
    if line < lines:
        print("")
