# def cat():
#     return "Meow"

# my_favorite_animal = cat

# print(my_favorite_animal)
def apply_operation(func, *args): # * = 가변 인자
    return func(args )

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

result = apply_operation(add, 2, 3)
print(result)