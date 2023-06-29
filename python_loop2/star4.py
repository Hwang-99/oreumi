# lines = int(input())

# for line in range(1, lines + 1):

#     for star in range((lines-line) + 1):
#         print("*", end='')
#     for blank in range (line):
#         print('', end='')
#     if line < lines:
#         print("")

# slicing 사용

lines = int(input())

for line in range(1, lines + 1):

    # 공백 생성 blank = line -1
    for i in range(line - 1):
        print(" ", end='')

    # 별 생성 star = lines - line
    for star in range((lines-line+1)):
        print("*", end='')

    if line < lines:
        print("")

lines = int(input())

for line in range(1, lines + 1):
    for i in range(line - 1):
        print(" ", end='')
    for star in range((lines-line+1)):
        print("*", end='')

    if line < lines:
        print("")