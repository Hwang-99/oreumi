numbers = [4, 2, 7, 1, 9, 5]

#최악의 경우, len(numbers)만큼 검색 == O(n)
# len(numbers) => n개라면
#for문 n번만큼 => 시간복잡도 O(n)

target_number = 7

for idx, i in enumerate(numbers):
    if i == target_number:
        print(idx)