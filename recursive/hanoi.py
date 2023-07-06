def hanoi(start, middle, end, n):
    if n == 1:
        print(start, end)
    else:
        hanoi(start, end, middle, n-1)
        print(start, end)
        hanoi(middle, start, end, n-1)

a = int(input(""))
hanoi(1, 2, 3, a)