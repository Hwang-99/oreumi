# a = int(input(""))

# for i in range(1, 10):
#     result = a * i
#     print(f"{a} * {i} = {result}")



#이중 반복문 (이중 for문)

star = int(input())
#input에서 받은 star를 int로 형변환
for i in range(1,star+1):
# 1부터 star+1 까지의 범위를 i 변수에 할당
    for j in range(star-i):   
        print(' ', end= '') 
    for k in range(i):
# i 변수에 할당된 범위를 j에 할당        
        print('*', end= '')
# '*'을 출력하고 end로 묶음      
    print()

star = int(input())
for i in range(1,star+1):
    for j in range(star-i):   
        print(' ', end= '') 
    for k in range(i):
        print('*', end= '')
    print()



