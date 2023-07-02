n = int(input())
list = []
for i in range(1, n + 1):
    a,b = map(int,input().split())
    list.append([a, b])

j=1
for i in list:
    print("Case #{}: {} + {} = {}".format(j, i[0], i[1], i[0]+i[1]))
    j+=1
    # list의 값을 i부터 차례대로 출력

# n = int(input())
# list = []
# for i in range(1, n + 1):
#     a,b = map(int,input().split())
#     list.append(a+b)
# print(list)
# j=1
# for i in list:
#     print("CASE #{}: {}".format(j, i ))
#     j+=1
    

