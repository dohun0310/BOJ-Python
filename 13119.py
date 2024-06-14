n, m, x = map(int, input().split())
h = list(map(int, input().split()))
l = [["."] * m for _ in range(n)]
for i in range(m):
    a = h[i]
    for j in range(n - 1, n - 1 - a, -1):
        l[j][i] = "#"
for i in range(m):
    if h[i] >= x:
        l[n - x][i] = "*"
    else:
        l[n - x][i] = "-"
        if (i + 1) % 3 == 0:
            for j in range(n - x + 1, n - h[i]):
                l[j][i] = "|"
for i in l:
    print("".join(i))