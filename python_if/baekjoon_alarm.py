# H, M = map(int, input().split())
# if M < 45:
#     print((H - 1), (M + 15))
# else:
#     print(H, (M - 45))

# H, M = map(int, input().split())
# if M < 45:
#     if H == 0:
#         H = 23
#         M += 15
#     else:
#         H -= 1
#         M += 15

# else:
#     M -= 45

# print(H, M)

H, M = map(int,input().split())
timer = int(input())

h = timer // 60    
m = timer % 60

H += h
M += m

if M > 59:
    M -= 60
    H += 1

if H > 23:
    H -= 24

print(H, M)