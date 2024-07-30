from collections import deque
def bfs(v, e, f, x, y):
    c = 1
    v[x][y] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + e[i]
            ny = y + f[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if v[nx][ny]:
                v[nx][ny] = 0
                q.append((nx, ny))
                c += 1
    return c
e = [-1, 1, 0, 0]
f = [0, 0, -1, 1]
n = int(input())
g = [[] for i in range(n)]
for i in range(n):
    g[i] = list(map(int, input()))
l = []
for i in range(n):
    for j in range(n):
        if g[i][j]:
            l.append(bfs(g, e, f, i, j))
l.sort()
print(len(l))
print(*l, sep="\n")