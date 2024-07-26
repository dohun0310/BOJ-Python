import sys
from collections import deque
def bfs(v, e, r, d):
    v[r] = 1
    d[r] = 0
    q = deque([r])
    while q:
        u = q.popleft()
        for i in e[u]:
            if not v[i]:
                v[i] = 1
                q.append(i)
                d[i] = d[u] + 1
n, m, k, x = map(int, sys.stdin.readline().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
for i in range(n + 1):
    g[i].sort()
v = [0] * (n + 1)
d = [0] * (n + 1)
bfs(v, g, x, d)
t = True
for i in range(len(d)):
    if d[i] == k:
        t = False
        print(d.index(d[i]))
        d[i] = 0
if t:
    print(-1)