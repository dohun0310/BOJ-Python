import sys
n = int(sys.stdin.readline())
m = [[0] * (n + 1)] + [[0] + list(map(int, sys.stdin.readline().split())) for i in range(n)]
l = [[[0] * 11 for i in range(n + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, 11):
            if k == m[i][j]:
                l[i][j][k] += 1
            l[i][j][k] += l[i - 1][j][k] + l[i][j - 1][k] - l[i - 1][j - 1][k]
q = int(sys.stdin.readline())
for i in range(q):
    a, b, x, y = map(int, sys.stdin.readline().split())
    s = 0
    for j in range(1, 11):
        if l[x][y][j] - l[x][b - 1][j] - l[a - 1][y][j] + l[a - 1][b - 1][j]:
            s += 1
    print(s)