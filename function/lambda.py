# def add(a, b):
#     return a + b

# add = lambda a, b: a+b
# result = add(2, 3)
# print(result)

# numbers = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x+1, numbers))
# #map은 for문이 돈다고 생각
# data = list(map(int, input().split()))


# print(squared)

# data = map(int, input().split()) # list

students = [
    {"name": "이민영","age":23},
    {"name": "양승조", "age":17},
    {"name": "문기원", "age":25}
]
students.sort(key=lambda x:x["age"]) # key = 키워드 인자
print(students)