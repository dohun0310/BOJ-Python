import sys
from collections import deque
def bfs(v, e, r):
    global c
    v[r] = c
    q = deque([r])
    while q:
        u = q.popleft()
        for x in e[u]:
            if not v[x]:
                c += 1
                v[x] = c
                q.append(x)
n, m, r = map(int, sys.stdin.readline().split())
c = 1
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)
for i in range(n + 1):
    g[i].sort(reverse=True)
v = [0] * (n + 1)
bfs(v, g, r)
for i in range(1, n + 1):
    print(v[i])