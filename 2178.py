from collections import deque
def bfs(v, e, f, x, y):
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + e[i]
            ny = y + f[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if v[nx][ny] == 0:
                continue
            if v[nx][ny] == 1:
                v[nx][ny] = v[x][y] + 1
                q.append((nx, ny))
e = [-1, 1, 0, 0]
f = [0, 0, -1, 1]
n, m = map(int, input().split())
g = [[] * m for i in range(n)]
for i in range(n):
    g[i] = list(map(int, input()))
bfs(g, e, f, 0, 0)
print(g[n - 1][m - 1])