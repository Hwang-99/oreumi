def substract(a, b):
    return a - b

def multiply(a, b = 2):
    return a * b

def sum(*args):
    total = 0
    for i in args:
        total+= i
    return total

def character_info(name, age, address, ip, computer, duration):
    print("이름", name)
    print("나이", age)

def database_login(address, ip, database):
    pass


database_login(ip="127.0.0.1", database="oreumi_database") #키워드 인자 