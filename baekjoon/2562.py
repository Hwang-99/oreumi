a = []
for i in range(9):
    num = int(input())
    a.append(num)

max_value = max(a)
max_index = a.index(max_value)

print(max_value)
print(max_index + 1)

# List Comprehension
a = [int(input()) for i in range(9)]; print(max(a));
print(a.index(max(a)))