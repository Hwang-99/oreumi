# list comprehension

numbers = [1, 2, 3, 4, 5]
# result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
result = ['even' if x % 2 == 0 else 'odd' for x in numbers]
# result = [x for x in numbers]
result = [x for x in numbers if x % 2 == 0] #짝수만 출력
print(result)