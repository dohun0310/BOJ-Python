for i in range(int(input())):
    n = int(input()) // 2
    x, y = n, n
    while x > 0:
        if all(x % i for i in range(2, int(x ** 0.5) + 1)) and all(y % i for i in range(2, int(y ** 0.5) + 1)):
            print(x, y)
            break
        else:
            x -= 1
            y += 1