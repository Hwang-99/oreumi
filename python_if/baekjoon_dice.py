x, y, z = map(int,input().split())
result = [x, y, z]

if x == y == z:
    print(10000 + x * 1000)

elif x == y:
    print(1000 + x * 100)
    
elif y == z:
    print(1000 + y * 100)

elif z == x:
    print(1000 + z * 100)

elif x != y != z :
    print((max(result)) * 100)

else :
    print("Type Error")
