a = int(input())


num_list = input().split(" ")
for idx, i in enumerate(num_list):
    num_list[idx] = int(i)
    
max = num_list[0]
min = num_list[0]

for i in num_list:
    if max < i:
        max = i
    if min > i:
        min = i
        
print(min, max)

    
    


