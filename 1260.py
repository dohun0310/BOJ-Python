from collections import deque
n, m, v = map(int, input().split())
g = [[False] * (n + 1) for i in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    g[x][y] = g[y][x] = True
d = [False] * (n + 1)
b = [False] * (n + 1)
def dfs(x):
    if d[x]: return
    d[x] = True
    print(x, end=' ')
    for i in range(1, n + 1):
        if g[x][i]: dfs(i)
def bfs(x):
    q = deque([x])
    b[x] = True
    while q:
        x = q.popleft()
        print(x, end=' ')
        for i in range(1, n + 1):
            if g[x][i] and not b[i]:
                q.append(i)
                b[i] = True
dfs(v)
print()
bfs(v)