import sys
from collections import deque
def bfs(v, e, f, x, y):
    v[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + e[i]
            ny = y + f[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if v[nx][ny] == 1:
                q.append((nx, ny))
                v[nx][ny] = 0
e = [-1, 1, 0, 0]
f = [0, 0, -1, 1]
for i in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().split())
    c = 0
    g = [[0] * n for j in range(m)]
    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        g[x][y] = 1
    for x in range(m):
        for y in range(n):
            if g[x][y] == 1:
                bfs(g, e, f, x, y)
                c += 1
    print(c)