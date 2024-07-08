n, l = map(int, input().split())
for i in range(l, 101):
    y = n - (i * (i + 1) // 2)
    if y % i == 0:
        x = y // i
        if x + 1 >= 0:
            print(*(i for i in range(x + 1, x + i + 1)))
            break
else:
    print(-1)