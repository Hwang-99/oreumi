# a = []

# for i in range(1,6):
#     a.append(i) # 추가



# for i in range(1, 6):
#     a.remove(i) # 삭제
# print(a)

#중복된 원소가 있다면 앞에서부터 제거(idx가 낮은 값부터)
#remove와 pop의 차이

# a = [1, 3, 5, 4 ,2 ,6 ,9 ,8 ,10 ,7]
# a.sort(reverse=True) #정렬
# print(a)

# a = [1, 2, 3, 4, 5, 6]
# print(a[3:5]) # slicing 사용 시 내가 원하는 범위 + 1을 해야 함
# print(a[3:])

# a = [i for i in range(1, 6)]
# print(a)

# a = [i**2 for i in range(1, 6)] # 제곱수 표현

# append
# remove
# sort

# 리스트 합치기

# a = [1, 2, 3]
# b = [4, 5, 6]

# a.extend(b)
# print(a)

# a = a + b
# print(a)

# a = a * 3
# print(a)

# a.insert(2, 4) # a[1] = 2
# print(a)

# a = ["1" ,"2", "3", "2"]
# # a.pop(2)
# # print(a)

# # index = a.index("1")
# # print(index)

# # print(len(a)) # 길이

# # print(a.count("2")) # "2"의 개수 계산
# # a.reverse()
# # print(a)

# # n = int(input())
# # a = [1, 2, 3]
# # for idx, i in enumerate(a):
# #     if i == n:
# #         print(idx)

# a = [1, "2", "3", 4]
# print(a.index("3"))

# # n = int(input())
# # a = [1, "2", 3, "4"]
# # print(a.index(n))
# #Q. 속성이 다른 요소들의 리스트에서 n을 입력받아서 index로 출력하려면?

# list.append() # list의 마지막에 요소 추가
# list.remove() # list의 해당하는 값 제거
# list.pop() # list의 해당하는 인덱스 요소 제거
# list.sort() # list의 오름차순 정렬
# list.reverse() # list의 내림차순 정렬
# list.extend() # list를 합침
# len(list) # list의 길이 측정
# list.index() # list의 인덱스 확인
# list.insert() # list에 요소 삽입

a = (1, 2, 3)
# a.append(4)
# a.remove(2)
# a.sort
# a.reverse
# a.extend
# len(a)        <--- O
# a.index(2)    <--- O
# a.count(2)    <--- O 

# a,b = input("").split(" ")
# point = 1, 2
# print(type(point)) 
# x, y = point

# def hello():
#     return "hello", "world!"

# x,y = hello()

a = {1, 2, 3} # set

