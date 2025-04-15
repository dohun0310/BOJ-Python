for i in range(int(input())):
    x, y = map(int, input().split())
    t, c, s = 0, 0, 0
    while t < y - x:
        c += 1
        if c % 2 == 1:
            s += 1
        t += s
    print(c)