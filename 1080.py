def f(x, y):
    for i in range(3):
        for j in range(3):
            a[x + i][y + j] = 1 - a[x + i][y + j]
n, m = map(int, input().split())
a = [list(map(int,list(input()))) for i in range(n)]
b = [list(map(int,list(input()))) for i in range(n)]
if a == b:
    print(0)
    exit()
c = 0
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            f(i, j)
            c += 1
        if a == b:
            print(c)
            exit()
else:
    print(-1)