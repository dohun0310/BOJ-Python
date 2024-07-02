import sys
n, m = map(int, sys.stdin.readline().split())
l = []
s = [[0] * (n + 1) for i in range(n + 1)]
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + l[i - 1][j - 1]
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(s[x2][y2] - s[x1 - 1][y2] - s[x2][y1 - 1] + s[x1 - 1][y1 - 1])