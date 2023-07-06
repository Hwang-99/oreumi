numbers = [1, 2, 3, 4, 5, 6] # N개가 주어졌다면


# O(N)
# sum = 0
# for i in numbers: # N번 돌아야함
#     sum += i


#O(1)
sum = (numbers[5] + 1) * len(numbers) / 2
print(int(sum))