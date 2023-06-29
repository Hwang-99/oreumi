# numbers = [1, 2, 2 ,3 ,3 ,5]
# set_numbers = set(numbers)
# print(len(set_numbers

# print(a.intersection(b)) # 교집합
# print(a-b)
# # print(a.union(b)) # 합집합
# print(a&b)
# # print(a.difference(b)) # 차집합
# print(a|b)

# a.add(4)
# print(a)
# a.remove(5)
# a.discard(5) # 없는 원소 제거 시 에러 발생 x
# print(a)

# a = {1, 2, 3, 5}
# b = {3, 5, 6, 7}

# is_sub = a.issubset(b) #a가 b에 포함되어 있는지 확인
# print(is_sub)

# print(a.symmetric_difference(b)) # 대칭 차집합

# a = [1, 2, 3] list
# a = (1, 2, 3) tuple
# a = {1, 2, 3} set

# a.clear()
# print(a)

# if 2 in a:
#     print(True)

# 교집합, 합집합, 차집합 만큼은 어느 때에 사용해야하는지 깨닫고, 기억
# 코드를 짤 때에는 가독성 또한 매우 중요 !

a = [1, 2, 3]
a = list(set(a))
print(a)




