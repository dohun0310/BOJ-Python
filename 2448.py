def d(x, y, n):
    if n == 3:
        a[x][y] = "*"
        a[x + 1][y - 1] = a[x + 1][y + 1] = "*"
        for i in range(-2, 3):
            a[x + 2][y + i] = "*"
    else:
        m = n // 2
        d(x, y, m)
        d(x + m, y - m, m)
        d(x + m, y + m, m)
n = int(input())
a = [[" " for j in range(2 * n)] for i in range(n)]
d(0, n - 1, n)
for i in a:
    print("".join(i))